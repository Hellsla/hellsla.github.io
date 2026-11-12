// Air:bit 2 -ohjaimen aloitusohjelma (Ruukkilabra, Dronelabra, tunti 5)
// MakeCode (makecode.microbit.org): vaihda JavaScript-nakymaan, liita ohjelma ja palaa lohkoihin.
// Testaamaton luonnos. Kokeile aina ensin ILMAN POTKUREITA: kaynnistyvatko ja pysahtyvatko moottorit hallitusti?
// Ohjain lahettaa viisi arvoa (valmistajan ohjeen "PARTY"): P = pitch, A = arm, R = roll, T = throttle, Y = yaw.
// Starter for the Air:bit 2 hand controller. Untested draft: always try it first WITHOUT PROPELLERS.

let radioGroup = 7      // vaihda ryhmasi omaksi numeroksi; dronessa pitaa olla sama / your group's own number, the same on the drone
let arm = 0             // 0 = moottorit eivat kay, 1 = kaynnistyslupa / 1 = the motors may run
let throttle = 0        // kaasu 0...100
let pitch = 0           // kallistus eteen ja taakse, asteina / forwards and backwards, degrees
let roll = 0            // kallistus sivulle, asteina / sideways, degrees

radio.setGroup(radioGroup)
basic.showNumber(radioGroup)

// A pienentaa kaasua, B kasvattaa. Yli 40:n askel on 1, jotta leijunnan saato on tarkkaa.
// A lowers the throttle, B raises it. Above 40 the step is 1 for a finer hover.
input.onButtonPressed(Button.A, function () {
    throttle = Math.max(0, throttle - (throttle > 40 ? 1 : 5))
})
input.onButtonPressed(Button.B, function () {
    throttle = Math.min(100, throttle + (throttle >= 40 ? 1 : 5))
})

// A+B yhta aikaa: kaynnistyslupa paalle tai pois. Kaasu nollataan aina samalla.
// A+B together: arm or disarm. The throttle always returns to zero.
input.onButtonPressed(Button.AB, function () {
    arm = arm == 0 ? 1 : 0
    throttle = 0
})

// Hatapysaytys: ravista ohjainta. / Emergency stop: shake the controller.
input.onGesture(Gesture.Shake, function () {
    arm = 0
    throttle = 0
})

basic.forever(function () {
    pitch = Math.constrain(input.rotation(Rotation.Pitch), -45, 45)
    roll = Math.constrain(input.rotation(Rotation.Roll), -45, 45)
    radio.sendValue("P", pitch)
    radio.sendValue("A", arm)
    radio.sendValue("R", roll)
    radio.sendValue("T", throttle)
    radio.sendValue("Y", 0)          // kaanto on jatkotehtava / yaw is an extra task

    // Naytto: vasen ylakulma = kaynnistyslupa, vasen sarake = kaasu, piste = kallistus
    // Display: top left = armed, left column = throttle, the dot = tilt
    basic.clearScreen()
    if (arm == 1) {
        led.plot(0, 0)
    }
    led.plot(0, 4 - Math.idiv(throttle, 25))
    led.plot(Math.round(Math.map(roll, -45, 45, 0, 4)), Math.round(Math.map(pitch, -45, 45, 0, 4)))
})

// Tarkista ilman potkureita, etta kallistuksen suunta vastaa dronen liiketta. Jos suunta on vaarin pain,
// vaihda arvon etumerkki (esimerkiksi radio.sendValue("P", -pitch)).
// Check without propellers that the tilt direction matches the drone. If it is reversed, change the sign.
