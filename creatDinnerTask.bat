SCHTASKS /Delete /TN dinner /F
SCHTASKS /Create /SC WEEKLY /D "MON THU SAT FRI WED TUE " /ST 11:00 /TN dinner /TR runDinner.exe