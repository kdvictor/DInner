SCHTASKS /Delete /TN applydinner4 /F
SCHTASKS /Create /SC WEEKLY /D "MON WED SAT" /ST 11:00 /TN applydinner4 /TR d:\dinner\run.bat