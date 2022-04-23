.data

.text
.frame add, 0, %vr1
    load %vr1 => %vr2
    loadI 1 => %vr3
    add %vr2, %vr3 => %vr4
    load %vr1 => %vr2
    store %vr4 => %vr1
    load %vr1 => %vr2
    iwrite %vr2
    ret
.frame main, 4 
    loadI 10 => %vr6
    i2i %vr6 => %vr7
    iwrite %vr7
    i2i %vr0 => %vr9
    loadI 0 => %vr8
    sub %vr9, %vr8 => %vr10
    store %vr7 => %vr10
    call add, %vr10
    load %vr10 => %vr11
    iwrite %vr11
    ret
