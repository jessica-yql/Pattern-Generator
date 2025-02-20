def add_suffix(num):
    if num % 100 in [11, 12, 13]:  # special cases for 11th, 12th, 13th
        suffix = "th"
    else:
        suffix_dict = {1: "st", 2: "nd", 3: "rd"}
        suffix = suffix_dict.get(num % 10, "th")
    return str(num) + suffix

def tube_top_pattern():
    
    gauge_sts = float(input("Enter number of stitches per inch: "))
    gauge_rows = float(input("Enter number of rows per inch: "))
    
    high_bust = float(input("Enter high bust measurement (in): "))
    bust = float(input("Enter bust measurement (in): "))
    waist = float(input("Enter waist measurment (in): "))
    hip = float(input("Enter hip measurment (in): "))


    high_bust_to_bust = float(input("Enter length from high bust to bust (in): "))    
    bust_to_waist = float(input("Enter length from bust to waist (in): "))
    waist_to_hip = float(input("Enter length from waist to hip (in): "))
    
    high_bust_sts = gauge_sts * high_bust
    stitch_marker = add_suffix(int(high_bust_sts / 2))
    bust_sts = gauge_sts * bust
    waist_sts = gauge_sts * waist
    hip_sts = gauge_sts * hip

    high_bust_to_bust_rows = gauge_rows * high_bust_to_bust
    bust_to_waist_rows = gauge_rows * bust_to_waist
    waist_to_hip_rows = gauge_rows * waist_to_hip

    bust_incr = bust_sts - high_bust_sts
    bust_incr_interval = high_bust_to_bust_rows / (bust_incr/4)

    waist_decr = bust_sts - waist_sts
    wait_decr_interval = bust_to_waist_rows / (waist_decr/4)
    
    
    pattern = f"""
    Top-Down Tube Top Pattern:
    1. Cast on {int(high_bust_sts) + 1} stitches for the high bust, placing a stitch marker after the {stitch_marker} cast on stitch.
    2. Join in the round and place a stitch marker. You should now have {int(high_bust_sts)} stitches. 
    3. Knit in the round for {int(bust_incr_interval - 1)} rows.
    4. On the {add_suffix(int(bust_incr_interval))} row, K1, M1L, then K until 1 stitch before the stitch marker, M1R, K2, M1L, then K until 1 stitch before the stitch marker and M1R.
    5. Repeat steps 3 and 4 until you have knit {int(high_bust_to_bust_rows)} rows and around {int(bust_sts)} stitches.
    4. Then, begin knitting in the round for {bust_to_waist_rows} rows, decreasing.
    5. Decrease to {waist_sts} stitches for the waistline.
    6. Knit for {waist_to_hip_rows} more rows.
    7. Increase to {hip_sts} stitches until the length reaches the hip line.
    8. Bind off all stitches and weave in all ends.
    """
    print(pattern)

tube_top_pattern()
