from currency_converter  import CurrencyConverter
c = CurrencyConverter()

def CostNormalization(df):

    liste_money = []

    for i in df["Cost"].values:
        if i == "€ 9,4 million":
            liste_money.append(c.convert(9.4 * 1000000, "EUR", "USD"))

        else:
            i = i.replace(',', '')
            if i.startswith("$"):
                liste = i[1:].split(' ')
                if len(liste) == 1:

                    if "million" in liste[0]:
                        liste_money.append(float(liste[0][:liste[0].find('m')]) * 1000000)

                    else:
                         liste_money.append(float(liste[0][:liste[0].find('[')]))

                else:    
                    if ("million" in liste[1] or "Million" in liste[1]) and "2020" not in liste:
                        liste_money.append(float(liste[0].split("–")[0]) * 1000000)

                    elif "USD" in liste[1] or "US" in liste[1]:
                        liste_money.append(float(liste[0]))

                    elif "000000" in liste[1]:
                        liste_money.append(float(liste[0]) * 1000000)

                    elif "M" in liste[0]:
                        liste_money.append(float(liste[0][:liste[0].find('M')]) * 1000000)

                    elif "CDN" in liste[1]:
                        liste_money.append(c.convert(float(liste[0]) , 'CAD', 'USD'))

                    elif "DKK" in liste[1]:
                        liste_money.append(c.convert(float(liste[0]) , 'DKK', 'USD'))

                    else:
                        liste_money.append(float(liste[0][:liste[0].find("(")]))
            elif i.startswith("€"):
                i = i[1:]

                if i[0] == ' ':
                    i = i[1:]

                if '[' in i:
                    i = i[:i.find('[')]

                if 'million' in i and '(' not in i:
                    liste_money.append(float(i[:i.find(' ')]) * 1000000)

                elif 'million' in i and '(' in i:
                    liste_money.append(19.9*1000000)

                else:
                    liste_money.append(float(i))

            elif i.startswith("US$"):
                i = i[3:]
                if i.startswith(' '):
                    i = i[1:]

                if '[' in i:
                    i = i[:i.find('[')]

                if ('million' in i or 'Million' in i) and '(' not in i:
                    liste_money.append(float(i[:i.find(' ')])* 1000000)

                elif ('million' in i or 'Million' in i) and '(' in i:
                    if '9.1' in i:
                        liste_money.append(2 * 1000000)
                    elif '11.1' in i:
                        liste_money.append(10 * 1000000)
                else:
                    liste_money.append(float(i))

            elif i.startswith("£"):
                i = i[1:]

                if '[' in i:
                    i = i[:i.find('[')]

                if "million" in i or "Million" in i:
                    liste_money.append(float(i[:i.find(' ')]) * 1000000)

                elif '(' in i:
                    i = i[:i.find('(')]
                    liste_money.append(float(i))

                else:
                    liste_money.append(float(i))

            elif i.startswith("A$"):
                i = i[2:]
                if '[' in i:
                    i = i[:i.find('[')]

                if 'million' in i:
                    liste_money.append(c.convert(float(i[:i.find(' ')]) * 1000000, "AUD", "USD"))

                else:
                    liste_money.append(c.convert(float(i), "AUD", "USD"))

            elif 'approx' in i or 'Approx' in i:
                if '[' in i:
                    i = i[:i.find('[')]

                if '$' in i and '(' not in i:
                    i = i[i.find('$')+1:i.find(')')]

                if '€' in i:
                    liste_money.append(c.convert(44.3 * 1000000, "EUR", "USD"))

                elif "SEK" not in i:
                    if 'million' in i:
                        liste_money.append(float(126 * 1000000))

                    else:
                        liste_money.append(float(i))
                else:
                    if "million" in i:
                        liste_money.append(c.convert(float(100 * 1000000), "SEK", "USD"))

                    else:
                        liste_money.append(c.convert(239000000, "SEK", "USD"))



            elif i.startswith('AU'):
                i = i[3:i.find('(')]

                i = i[:i.find(' ')]
                liste_money.append(c.convert(float(i*1000000), "AUD", "USD"))

            elif "USD" in i:
                if i.startswith("USD"):
                    i = i[i.find("USD") + 3:]

                if i.startswith(' '):
                    i = i[1:]
                if i.startswith('$'):
                    i = i[1:i.find('[')]

                if 'USD' in i and '(' not in i:
                    i = i[:i.find("U")-1]

                if 'Yen' not in i and 'SEK' not in i:
                    if 'million' in i:
                        liste_money.append(float(300 * 1000000))

                    else:
                        liste_money.append(float(i))

                elif 'Yen' in i:
                    liste_money.append(c.convert(float(i[:i.find("Y") -1]), "JPY", "USD"))

                else:
                    liste_money.append(c.convert(float(110 * 1000000), "SEK", "USD"))


            elif '¥' in i or 'JPY' in i or 'yen' in i:
                if i.startswith('¥'):
                    i = i[1:]
                if i.startswith('J'):
                    i = i[4:]

                if 'billion' in i:
                    liste_money.append(c.convert(2.5 * 1000000000, "JPY", "USD"))

                elif 'million' in i:
                    liste_money.append(c.convert(float(450 * 1000000), "JPY", "USD"))

                else:
                    liste_money.append(c.convert(float(i), "JPY", "USD"))

            elif 'VND' in i:
                i = i[4:]

                i = i[:i.find("b") - 1]
                liste_money.append(float(i) * 1000000000 * 0.0000401400)

            elif '$' in i:


                if i.startswith("CA"):
                    i = i[3:i.find('[')]

                if i.startswith("C"):
                    i = i[2:]

                if '14' in i:
                    liste_money.append(float(14 * 1000000))

                elif '9' in i:
                    liste_money.append(float(9 * 1000000))

                else:
                    liste_money.append(float(26 * 1000000))

            elif '€' in i:
                if '26' in i:
                    liste_money.append(c.convert(float(26 * 1000000), 'EUR', "USD"))

                elif "FIM" in i:
                    liste_money.append(float(22000000) * 0.174341)

                else:
                    liste_money.append(c.convert(float(75 * 1000000), 'DKK', 'USD'))

            elif 'SEK' in i:
                if 'million' in i:
                    liste_money.append(c.convert(float(35 * 1000000), "SEK", "USD"))

                else:
                    liste_money.append(c.convert(float(50000000), "SEK", "USD"))

            elif "GB" in i:
                liste_money.append(c.convert(float(300000), "GBP", "USD"))

            elif "FIM" in i:
                liste_money.append(float(48 * 1000000) * 0.174341)


            elif "RMB" in i:
                liste_money.append(c.convert(float(90000000), "CNY", "USD"))

            elif "million" in i:
                liste_money.append(c.convert(float(3 * 1000000), 'EUR', "USD"))

            elif "Euro" in i:
                liste_money.append(c.convert(float(12 * 1000000), "EUR", "USD"))

            elif "Million" in i:
                liste_money.append(2.5 * 1000000)

            else:
                liste_money.append(1.2 * 1000000)
                
    return liste_money