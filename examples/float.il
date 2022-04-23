.data
    .float .float_const_0, 11.90000000
    .float .float_const_1, 2.58760000
.text
.frame myadd, 0, %vr1, %vr2
    f2i %vr2 => %vr3
    add %vr1, %vr3 => %vr4
    iret %vr4
.frame main, 4 
    loadI 1 => %vr5
    loadI .float_const_0 => %vr6
    fload %vr6 => %vr7
    icall myadd, %vr5, %vr7 => %vr8
    i2i %vr8 => %vr9
    iwrite %vr9
    loadI 2 => %vr10
    i2f %vr10 => %vr11
    fwrite %vr11
    loadI .float_const_1 => %vr12
    fload %vr12 => %vr13
    f2i %vr13 => %vr14
    iwrite %vr14
    ret
