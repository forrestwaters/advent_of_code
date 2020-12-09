from utils import read_input

input = read_input("day4.txt")
idx = 0
passports = []
for row in input:
    if len(passports) != idx + 1:
        passports.append({})
    if row == "":  # indicates new passport entry
        idx += 1
        continue
    for field in row.split(" "):
        k, v = field.split(":")
        passports[idx][k] = v

passport_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
def pt1(passports: "list[dict[str,str]]"):
  valid = 0
  for passport in passports:
    if "cid" in passport:
      del passport["cid"]
    if set(passport.keys()) == passport_fields:
      valid += 1
  return valid

valid_haircolors = {"a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
valid_eyecolors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
def pt2(passports: "list[dict[str,str]]"):
    valid = 0
    for passport in passports:
        if "cid" in passport:
            del passport["cid"]
        if set(passport.keys()) == passport_fields:
            if passport["byr"].isdigit() and 1920 <= int(passport["byr"]) <= 2002:
              if passport["iyr"].isdigit() and 2010 <= int(passport["iyr"]) <= 2020:
                if passport["eyr"].isdigit() and 2020 <= int(passport["eyr"]) <= 2030:
                  hgt = passport["hgt"].rstrip("\n")[:-2]
                  metric = passport["hgt"].replace(passport["hgt"][:-2], "")
                  if metric not in {"in", "cm"}:
                    continue
                  if metric == "in":
                    if not(59 <= int(hgt) <= 76):
                      continue
                  if metric == "cm":
                    if not (150 <= int(hgt) <= 193):
                      continue
                  if passport["pid"].isdigit() and len(passport["pid"]) == 9:
                    if passport["hcl"].startswith("#") and len(passport["hcl"]) == 7:
                      for x in passport["hcl"]:
                        if x not in valid_haircolors:
                          continue
                      if passport["ecl"] in valid_eyecolors:
                        valid += 1
    return valid


print(pt1(passports))
print(pt2(passports))