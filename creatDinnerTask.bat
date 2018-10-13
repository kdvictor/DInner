SCHTASKS /Delete /TN dinner /F
SCHTASKS /Create /SC WEEKLY /D "SAT MON THU WED TUE FRI " /ST 11:00 /TN dinner /TR d:\dinner\run.bat