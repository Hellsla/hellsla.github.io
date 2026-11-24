VERDICT: PASS
CONTENT-HASH: e099a0ff33b8b15c

## Blocking

## Polish
- solutions.md:176–179 (fy3-16-L3-03): the Kaava now ends at $m = E_\text{yht}/(c_\text{jää}\Delta T_\text{jää} + s)$, but the Sijoitus never names $E_\text{yht}$. Adding a row "$E_\text{yht} = 486\,000\,\text{J} + 50\,280\,\text{J} = 536\,280\,\text{J}$" before "Pienin massa" would make the Sijoitus substitute into the last symbolic form literally.
- solutions.md:167–169 (L3-03): $E_\text{yht}$ is the same quantity as $Q_\text{luovutettu}$, written out once more. Writing "$Q_\text{luovutettu} = E_\text{yht} = UA\Delta T\,t + c\,m_\text{j}\Delta T_\text{j}$" on one row would remove the duplicate.

## Checked
- solutions.md:163–171 (L3-03): I read the block on disk as an aligned block. There is no `array` numerator any more. The rows go from $Q_\text{vastaanotettu} = Q_\text{luovutettu}$ to $Q_\text{vastaanotettu} = m(c_\text{jää}\Delta T_\text{jää} + s)$, $P = UA\Delta T$, $E = Pt$, $Q_\text{luovutettu} = E + c\,m_\text{j}\Delta T_\text{j}$ and $E_\text{yht}$, ending with $m = E_\text{yht}/(c_\text{jää}\Delta T_\text{jää} + s)$. Every row is algebraically right, and the wall energy is now on the received side together with the drinks' heat, which settles my earlier polish point.
- The physics is unchanged: the ice warms from $-10\,{}^\circ\text{C}$ to $0\,{}^\circ\text{C}$ and then melts. The inside stays at $0\,{}^\circ\text{C}$, so the wall power is constant, as the task assumes.
- Recomputed: $(1{,}5 \cdot 0{,}50 \cdot 30 \cdot 21\,600 + 4190 \cdot 0{,}50 \cdot 24)/(2100 \cdot 10 + 334\,000) = 1{,}511\,\text{kg}$. This minimum is rounded up to $1{,}6\,\text{kg}$, which is the safe side.
- No other file and no answer, unit or tolerance changed. My previous checks still hold.
- The hash was the same at the start and the end.
