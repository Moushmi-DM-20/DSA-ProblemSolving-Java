#PF Calculation

#Solution
DA = "{BASIC}*0.40"
HRA = "{BASIC}+{DA}*0.30"
PF = "{BASIC}+{DA}+{HRA}*0.0833"

intBasic = int(input("Enter basic salary : "))
DA = DA.replace("{BASIC}",str(intBasic))
HRA = HRA.replace("{BASIC}",str(intBasic)).replace("{DA}", str(DA))
PF = PF.replace("{BASIC}",str(intBasic)).replace("{DA}", str(DA)).replace("{HRA}", str(HRA))
print(eval(DA))
print(eval(HRA))
print(eval(PF))
