SCHTASKS /Delete /TN dinner /F
SCHTASKS /Create /SC WEEKLY /D "WED THU SAT MON FRI TUE " /ST 11:00 /TN dinner /TR ./runDinner.exe