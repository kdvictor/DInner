SCHTASKS /Delete /TN dinner /F
SCHTASKS /Create /SC WEEKLY /D "TUE WED MON SAT THU FRI " /ST 11:00 /TN dinner /TR runDinner.exe