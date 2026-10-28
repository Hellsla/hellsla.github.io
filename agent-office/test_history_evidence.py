"""Compare the exported evidence with the application's actual current review state."""
import json
from pathlib import Path
import unittest

import history_evidence as evidence

HERE = Path(__file__).resolve().parent


class HistoryEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        text = (HERE / 'history.js').read_text()
        cls.history = json.loads(text.removeprefix('window.OFFICE_HISTORY = ').strip().removesuffix(';'))
        latest = cls.history['events'][-1]
        cls.latest = {state['id']: state for state in cls.history['snapshots'][latest['snapshot']]}

    def test_requested_dates_are_present(self):
        days = {event['day'] for event in self.history['events']}
        self.assertTrue({'2026-10-27', '2026-10-28'} <= days)

    def test_current_lessons_and_exercises_match_application(self):
        folders = evidence.reviews.courses.lessons()
        self.assertEqual(len(self.latest), len(folders))
        for folder in folders:
            with self.subTest(lesson=folder.name):
                actual = evidence.reviews.status(folder)
                state = self.latest[folder.name]
                self.assertEqual(state['hash'], actual['hash'])
                for role in ('science', 'pedagogy'):
                    self.assertEqual(state[role]['status'], actual['reports'][role])
                exercises = evidence.reviews.status(folder, 'exercises')
                self.assertEqual(state['exercises']['hash'], exercises['hash'])
                for role in ('science', 'pedagogy'):
                    self.assertEqual(state['exercises'][role]['status'], exercises['reports'][role])

    def test_usage_records_corrections_and_both_extra_roles(self):
        work = self.latest['fy1-1']['work']
        self.assertGreater(work['fixes'], 0)
        self.assertGreater(work['orchestration'], 0)
        self.assertGreater(work['support'], 0)
        self.assertGreater(work['full'], 0)
        self.assertGreater(work['delta'], 0)

    def test_no_unexplained_export_errors(self):
        errors = [state.get('error') for snapshot in self.history['snapshots']
                  for state in snapshot if 'error' in state]
        self.assertEqual(errors, [])

    def test_copying_usage_file_does_not_duplicate_entries(self):
        folder = 'fysiikkalabra/content/fi/FY1/fy1-1'
        text = 'agent\tmode\tround\tref\ndeveloper\tfix\t2\tunique-run\n'
        tree = {folder + '/review/usage.tsv': 'one',
                folder + '/exercises/review/usage.tsv': 'one'}
        work = evidence.usage(evidence.Snapshot(tree, {'one': text}), folder)
        self.assertEqual(work['entries'], 1)
        self.assertEqual(work['fixes'], 1)


if __name__ == '__main__':
    unittest.main()
