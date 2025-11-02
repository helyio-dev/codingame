from decimal import Decimal, ROUND_HALF_UP

time_str = input()
hh = int(time_str[0:2])
mm = int(time_str[3:5])
ss = int(time_str[6:8])
tz_sign = 1 if time_str[12] == '+' else -1
tz_hh = int(time_str[13:15])
tz_mm = int(time_str[16:18])
total_seconds = hh * 3600 + mm * 60 + ss
tz_offset_seconds = tz_sign * (tz_hh * 3600 + tz_mm * 60)
utc_seconds = total_seconds - tz_offset_seconds
biel_seconds = (utc_seconds + 3600) % 86400
beats = Decimal(biel_seconds) / Decimal('86.4')
beats = beats.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
print(f"@{beats}")
