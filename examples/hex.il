.data

.text
.frame printhex, 4, %vr1
    iwrite %vr1
    loadI 0 => %vr2
    comp %vr1, %vr2 => %vr3
    testle %vr3 => %vr4
    cbr %vr4 -> .L1
.L0: nop
    loadI 16 => %vr5
    mod %vr1, %vr5 => %vr6
    i2i %vr6 => %vr7
    loadI 10 => %vr8
    comp %vr7, %vr8 => %vr9
    testge %vr9 => %vr10
    cbr %vr10 -> .L2
    iwrite %vr7
    jumpI -> .L3
.L2: nop
    loadI 10 => %vr8
    comp %vr7, %vr8 => %vr11
    testne %vr11 => %vr12
    cbr %vr12 -> .L4
    loadI 65 => %vr13
    putchar %vr13
    jumpI -> .L3
.L4: nop
    loadI 11 => %vr14
    comp %vr7, %vr14 => %vr15
    testne %vr15 => %vr16
    cbr %vr16 -> .L5
    loadI 66 => %vr17
    putchar %vr17
    jumpI -> .L3
.L5: nop
    loadI 12 => %vr18
    comp %vr7, %vr18 => %vr19
    testne %vr19 => %vr20
    cbr %vr20 -> .L6
    loadI 67 => %vr21
    putchar %vr21
    jumpI -> .L3
.L6: nop
    loadI 13 => %vr22
    comp %vr7, %vr22 => %vr23
    testne %vr23 => %vr24
    cbr %vr24 -> .L7
    loadI 68 => %vr25
    putchar %vr25
    jumpI -> .L3
.L7: nop
    loadI 14 => %vr26
    comp %vr7, %vr26 => %vr27
    testne %vr27 => %vr28
    cbr %vr28 -> .L8
    loadI 69 => %vr29
    putchar %vr29
    jumpI -> .L3
.L8: nop
    loadI 70 => %vr30
    putchar %vr30
    jumpI -> .L3
.L9: nop
.L3: nop
    loadI 4 => %vr31
    rshift %vr1, %vr31 => %vr32
    i2i %vr32 => %vr1
    loadI 0 => %vr2
    comp %vr1, %vr2 => %vr3
    testle %vr3 => %vr4
    cbrne %vr4 -> .L0
.L1: nop
    ret
.frame main, 0 
    loadI 144 => %vr33
    call printhex, %vr33
    ret
