.data
    .string .str_const_0, "swap"
.text
.frame main, 20 
    loadI 0 => %vr5
    loadI 0 => %vr5
    i2i %vr0 => %vr4
    loadI 12 => %vr9
    sub %vr4, %vr9 => %vr10
    loadI -4 => %vr2
    add %vr10, %vr2 => %vr7
    loadI 4 => %vr3
    mult %vr5, %vr3 => %vr6
    sub %vr7, %vr6 => %vr8
    store %vr5 => %vr8
    loadI 1 => %vr11
    loadI 1 => %vr11
    i2i %vr0 => %vr10
    loadI 12 => %vr9
    sub %vr10, %vr9 => %vr15
    loadI -4 => %vr2
    add %vr15, %vr2 => %vr13
    loadI 4 => %vr3
    mult %vr11, %vr3 => %vr12
    sub %vr13, %vr12 => %vr14
    store %vr11 => %vr14
    loadI 2 => %vr16
    loadI 2 => %vr16
    i2i %vr0 => %vr15
    loadI 12 => %vr9
    sub %vr15, %vr9 => %vr20
    loadI -4 => %vr2
    add %vr20, %vr2 => %vr18
    loadI 4 => %vr3
    mult %vr16, %vr3 => %vr17
    sub %vr18, %vr17 => %vr19
    store %vr16 => %vr19
    i2i %vr20 => %vr1
    i2i %vr1 => %vr21
    loadI .str_const_0 => %vr22
    swrite %vr22
    loadI 0 => %vr5
    i2i %vr21 => %vr4
    loadI -4 => %vr2
    add %vr4, %vr2 => %vr7
    loadI 4 => %vr3
    mult %vr5, %vr3 => %vr6
    sub %vr7, %vr6 => %vr8
    load %vr8 => %vr23
    i2i %vr23 => %vr24
    loadI 2 => %vr16
    i2i %vr21 => %vr4
    loadI -4 => %vr2
    add %vr4, %vr2 => %vr7
    loadI 4 => %vr3
    mult %vr16, %vr3 => %vr17
    sub %vr7, %vr17 => %vr25
    load %vr25 => %vr26
    loadI 0 => %vr5
    i2i %vr21 => %vr4
    loadI -4 => %vr2
    add %vr4, %vr2 => %vr7
    loadI 4 => %vr3
    mult %vr5, %vr3 => %vr6
    sub %vr7, %vr6 => %vr8
    store %vr26 => %vr8
    loadI 2 => %vr16
    i2i %vr21 => %vr4
    loadI -4 => %vr2
    add %vr4, %vr2 => %vr7
    loadI 4 => %vr3
    mult %vr16, %vr3 => %vr17
    sub %vr7, %vr17 => %vr25
    store %vr24 => %vr25
    loadI 0 => %vr5
    i2i %vr5 => %vr27
    loadI 3 => %vr28
    comp %vr27, %vr28 => %vr29
    testge %vr29 => %vr30
    cbr %vr30 -> .L1
.L0: nop
    i2i %vr21 => %vr4
    loadI -4 => %vr2
    add %vr4, %vr2 => %vr7
    loadI 4 => %vr3
    mult %vr27, %vr3 => %vr31
    sub %vr7, %vr31 => %vr32
    load %vr32 => %vr33
    iwrite %vr33
    loadI 1 => %vr11
    add %vr27, %vr11 => %vr34
    i2i %vr34 => %vr27
    loadI 3 => %vr28
    comp %vr27, %vr28 => %vr29
    testge %vr29 => %vr30
    cbrne %vr30 -> .L0
.L1: nop
    ret
