class htmlcreator:
    def __init__(self):
        self.htmlstr="<html><title>kartta</title><body>"
        self.htmlmtr=["<font color=#ff9090>00 </font>", "<font color=#90ff90>01 </font>",
                  "<font color=#9090ff>02 </font>", "<font color=#900000>03 </font>",
                  "<font color=#009000>04 </font>", "<font color=#000090>05 </font>",
                  "<font color=#ffff00>06 </font>", "<font color=#ff00ff>07 </font>",
                  "<font color=#00ffff>08 </font>", "<font color=#909000>09 </font>",
                  "<font color=#900090>10 </font>", "<font color=#646432>11 </font>",
                  "<font color=#643264>12 </font>", "<font color=#326464>13 </font>",
                  "<font color=#643232>14 </font>", "<font color=#326432>15 </font>",
                  "<font color=#323264>16 </font>", "<font color=#646400>17 </font>",
                  "<font color=#640064>18 </font>", "<font color=#006464>19 </font>",
                  "<font color=#640000>20 </font>", "<font color=#006400>21 </font>",
                  "<font color=#000064>22 </font>", "<font color=#ffff20>23 </font>",
                  "<font color=#ff20ff>24 </font>", "<font color=#20ffff>25 </font>",
                  "<font color=#004080>26 </font>", "<font color=#008040>27 </font>",
                  "<font color=#400080>28 </font>", "<font color=#800040>29 </font>",
                  "<font color=#804000>30 </font>", "<font color=#408000>31 </font>",
                  "<font color=#008888>32 </font>", "<font color=#880088>33 </font>",
                  "<font color=#888800>34 </font>", "<font color=#000088>35 </font>",
                  "<font color=#008800>36 </font>", "<font color=#880000>37 </font>",
                  "<font color=#ff8800>38 </font>", "<font color=#0088ff>39 </font>",
                  "<font color=#0000ff>99 </font>", "<font color=#000000>** </font>",
                  "<font color=#22ff22>88 </font>", "<font color=#44ff44>77 </font>",]
        self.htmlbr="<br>"
        self.htmlend="</body></html>"

    def alku(self):
        s=self.htmlstr
        return s

    def ruutu(self, kartta):
        if kartta==99:kartta=40
        elif kartta == 88:kartta = 42
        elif kartta == 77:kartta = 43
        return self.htmlmtr[kartta]

    def breik(self):
        return self.htmlbr

    def loppu(self):
        return self.htmlend

