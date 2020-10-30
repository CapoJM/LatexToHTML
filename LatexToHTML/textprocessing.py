def changeDollar(s):
    """ This function changes the $ sign for [\latex] and so on for a string
    that represents a single line.
    """
    sout = ""
    isEquation = False
    isEnv = False
    for i in range(len(s)):
        if i == 0:
            if s[i] == "$":
                sout = sout + "[latex]"
                isEquation = True
            elif s[i] == "\\":
                continue
            else:
                sout = sout + s[i]
        else:
            if s[i] == "$" and s[i-1] != "\\":
                if isEquation:
                    sout = sout + "[/latex]"
                    isEquation = False
                else:
                    sout = sout + "[latex]"
                    isEquation = True
            elif s[i] == "$" and s[i-1] == "\\":
                sout = sout + "$"
            elif s[i] == "\\":
                continue
            else:
                if s[i-1] != "\\":
                    sout = sout + s[i]
                else:
                    sout = sout + "\\" + s[i]

    if sout.find("{\\bf") != -1:
        n = sout.find("{\\bf")
        sout = sout[:n] + "<strong>" + sout[n+5:]
        m = sout[n:].find("}")
        sout = sout[:n+m] + "</strong>" + sout[n+m+1:]


    return(sout)


def processArticle(latex):
    lineas = latex.split("\r\n")
    html = "&nbsp;\n"

    isList = False
    isEquation = False
    isExercise = False
    isQuestion = False
    isAnswer = False
    firstLineQuestions = False
    noQuestion = 0
    noItem = 0

    for s in lineas:
        s = s.strip()
        if s == '' or s.isspace():
            continue
        elif s.startswith("\\section"):
            html = html + "<h1>" + s[9:-1] + "</h1>\n&nbsp;\n"
            continue
        elif s.startswith("\\subsection"):
            html = html + "<h2 class=\"tit-sol\">" + s[12:-1] + "</h2>\n&nbsp;\n"
            continue
        elif s.startswith("\\subsubsection"):
            html = html + "<h3 id=\"des_pol\" class=\"r\">" + s[15:-1] + "</h3>\n&nbsp;\n"
            continue
        elif s.startswith("\\begin{itemize}"):
            # empieza lista:
            isList = True
            if s[15:].isspace() or s[15:] == '':
                continue
            else:
                s = s[15:]
        elif s.startswith("\\end{itemize}"):
            # empieza lista:
            isList = False
            noItem = 0
            if s[15:].isspace() or s[15:] == '':
                continue
            else:
                s = s[15:]
        elif s.startswith("\\begin{exer}"):
            # empieza lista:
            firstLineQuestions = True
            html += "\n<!-------Beginning of the question "+str(noQuestion + 1)+"-------->\n<div class=\"bloque clear\">\n"
            if s[12:].isspace() or s[12:] == '':
                continue
            else:
                s = s[12:]
        elif s.startswith("\\end{exer}"):
            # empieza lista:
            html += "</div>\n</div>\n<!-------End of question "+str(noQuestion + 1)+"-------->\n"
            noQuestion += 1
            if s[10:].isspace() or s[10:] == '':
                continue
            else:
                s = s[10:]
        elif s.startswith("\\begin{q}"):
            # empieza lista:
            if s[9:].isspace() or s[9:] == '':
                continue
            else:
                s = s[9:]
        elif s.startswith("\\end{q}"):
            # empieza lista:
            html += "<div class=\"vea\">\n\n<button type=\"button\">Solución</button>\n"
            if s[7:].isspace() or s[7:] == '':
                continue
            else:
                s = s[7:]
        elif s.startswith("\\begin{ans}"):
            # empieza lista:
            html += "<div class=\"solution\"><section>\n"
            if s[11:].isspace() or s[11:] == '':
                continue
            else:
                s = s[11:]
        elif s.startswith("\\end{ans}"):
            # empieza lista:
            html += "</section></div>\n"
            if s[9:].isspace() or s[9:] == '':
                continue
            else:
                s = s[9:]
        elif s.startswith("\\begin{align}") or s.startswith("\\begin{align*}") or s.startswith("{\\begin{align}") or s.startswith("{\\begin{align*}"):
            # empieza ecuación:
            isEquation = True
            if isList:
                html = html + "<p class=\"b\" style=\"text-align: center;\">[latex]\\begin{align*}\n"
            else:
                html = html + "<p class=\"b\"> [latex]\\begin{align*}\n"
            continue
        elif s.startswith("\\end{align}") or s.startswith("\\end{align*}") or s.startswith("\\end{align}}") or s.startswith("\\end{align*}}"):
            # empieza ecuación:
            isEquation = False
            html = html + "\\end{align*}[/latex]</p>\n&nbsp;\n"
            continue
        elif s.startswith("\\["):
            # empieza ecuación:
            isEquation = True
            if isList:
                html = html + "<p class=\"b\" style=\"text-align: center;\">[latex]\\displaystyle "
            else:
                html = html + "<p class=\"b\"> [latex]\\displaystyle "
            if s[2:].isspace() or s == '':
                continue
            else:
                s = s[2:]
        elif s.startswith("\\]"):
            isEquation = False
            html = html + "[/latex]</p>\n&nbsp;\n"
            if s[2:].isspace() or s == '':
                continue
            else:
                s = s[2:]

        if not isEquation:
            s = changeDollar(s)

        if s == '' or s.isspace():
            continue
        elif isList:
            if s.startswith("\\item"):
                html = html + "<p class=\"b\"><span class=\"sb\">" + str(noItem + 1) + "</span>" + s[5:] + "</p>\n&nbsp;\n"
                noItem +=1
            elif isEquation:
                html = html + s
            else:
                html = html + "<p class=\"b\">" + s + "</p>\n&nbsp;\n"
        elif isEquation:
            html = html + s
        elif firstLineQuestions:
            html = html + "<p class=\"a\"><span class=\"sb\">"+str(noQuestion + 1)+"</span> " + s + "</p>\n&nbsp;\n"
            firstLineQuestions = False
        else:
            html = html + "<p class=\"a\">" + s + "</p>\n&nbsp;\n"

    return html


def processComment(latex):
    html = ""

    return html
