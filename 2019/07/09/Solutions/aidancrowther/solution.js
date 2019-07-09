function isHappy(val){ let newval = 0; while(val){ newval += (val%10)**2; val = Math.floor(val/10); } newval == 1 ? newval = true : newval = isHappy(newval); return newval}
