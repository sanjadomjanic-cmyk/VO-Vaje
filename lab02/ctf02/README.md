# Level 0
```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
# password: bandit0
ls
cat readme
exit
```

# Level 1
```bash
# password: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If
exit
ssh bandit1@bandit.labs.overthewire.org -p 2220
cat ./- 
password: 263JGJPfgU6LtdEvgfWU1XP5yac29mFx
exit
```

# Level 2
```bash
ssh bandit2@bandit.labs.overthewire.org -p 2220
cat ./--spaces\ in\ this\ filename--
# password: MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
```

# Level 3
```bash
ssh bandit3@bandit.labs.overthewire.org -p 2220
cd inhere
ls -la
cat ...Hiding-From-You
# password: 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
exit
```

# Level 4
```bash

ssh bandit4@bandit.labs.overthewire.org -p 2220
cat ./-file07
# password: 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
```

# Level 5
```bash
ssh bandit5@bandit.labs.overthewire.org -p 2220
man find | grep size
find . -size 1033c
cat ./maybehere07/.file2
# password: HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
exit
```

# Level 6
```bash
ssh bandit6@bandit.labs.overthewire.org -p 2220
man find | grep user
man find | grep group
find / -user bandit7 -group bandit6
find / -user bandit7 -group bandit6 2>/dev/null
find / -user bandit7 -group bandit6 | grep "password"
cat /var/lib/dpkg/info/bandit7.password
# password: morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
exit
```

# Level 7
```bash
ssh bandit7@bandit.labs.overthewire.org -p 2220
cat data.txt | grep millionth
# password: dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
```

# Level 8
```bash
ssh bandit8@bandit.labs.overthewire.org -p 2220
cat data.txt
sort data.txt
sort data.txt | uniq -u
# password: 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
```

# Level 9
```bash
ssh bandit9@bandit.labs.overthewire.org -p 2220
cat data.txt | grep "="
strings data.txt | grep "="
# password: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
```

# Level 10
```bash
ssh bandit10@bandit.labs.overthewire.org -p 2220
man base64
base64 -d data.txt 
# password: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
```

# Level 11
```bash
ssh bandit11@bandit.labs.overthewire.org -p 2220
tr 'A-Za-z' 'N-ZA-Mn-za-m' < data.txt 
# password: 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
```

# Level 12
