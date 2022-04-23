.data

.text
.frame gcd, 0, %vr1, %vr2
    loadI 0 => %vr3
    comp %vr2, %vr3 => %vr4
    testne %vr4 => %vr5
    cbr %vr5 -> .L0
    iret %vr1
    jumpI -> .L1
.L0: nop
    mod %vr1, %vr2 => %vr6
    icall gcd, %vr2, %vr6 => %vr7
    iret %vr7
.L1: nop
.frame main, 8 
    loadI 0 => %vr3
    i2i %vr3 => %vr8
    loadI 0 => %vr3
    i2i %vr3 => %vr9
    i2i %vr0 => %vr10
    loadI 0 => %vr3
    sub %vr10, %vr3 => %vr11
    store %vr8 => %vr11
    iread %vr11
    i2i %vr0 => %vr10
    loadI 4 => %vr12
    sub %vr10, %vr12 => %vr13
    store %vr9 => %vr13
    iread %vr13
    load %vr11 => %vr14
    loadI 0 => %vr3
    comp %vr14, %vr3 => %vr15
    testeq %vr15 => %vr16
    load %vr13 => %vr17
    loadI 0 => %vr3
    comp %vr17, %vr3 => %vr18
    testeq %vr18 => %vr19
    or %vr16, %vr19 => %vr20
    cbr %vr20 -> .L3
.L2: nop
    load %vr11 => %vr14
    load %vr13 => %vr17
    icall gcd, %vr14, %vr17 => %vr7
    iwrite %vr7
    load %vr11 => %vr14
    i2i %vr0 => %vr10
    loadI 0 => %vr3
    sub %vr10, %vr3 => %vr11
    store %vr14 => %vr11
    iread %vr11
    load %vr13 => %vr17
    i2i %vr0 => %vr10
    loadI 4 => %vr12
    sub %vr10, %vr12 => %vr13
    store %vr17 => %vr13
    iread %vr13
    load %vr11 => %vr14
    loadI 0 => %vr3
    comp %vr14, %vr3 => %vr15
    testeq %vr15 => %vr16
    load %vr13 => %vr17
    loadI 0 => %vr3
    comp %vr17, %vr3 => %vr18
    testeq %vr18 => %vr19
    or %vr16, %vr19 => %vr20
    cbrne %vr20 -> .L2
.L3: nop
    ret
