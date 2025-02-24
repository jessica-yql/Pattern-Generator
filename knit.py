def add_suffix(num):
    if num % 100 in [11, 12, 13]: 
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
    waist_decr = bust_sts - waist_sts
    hip_incr = hip_sts - waist_sts

    # Cast on
    pattern = f"""
    Top-Down Tube Top Pattern:
        Cast on {int(high_bust_sts) + 1} stitches for the high bust, placing a stitch marker after the {stitch_marker} cast on stitch.
        Join in the round and place a stitch marker. You should now have {int(high_bust_sts)} stitches. 
    """

    # High Bust to Bust
    if bust_incr != 0:
        bust_incr_interval = high_bust_to_bust_rows / (bust_incr/4)
        incr_1 = f"""
        * Knit in the round for {int(bust_incr_interval - 1)} rows.
        On the {add_suffix(int(bust_incr_interval))} row, K1, M1L, then K until 1 stitch before the stitch marker, M1R, K2, M1L, then K until 1 stitch before the stitch marker and M1R, K1. *
        Repeat the steps between the * * until you have knit {int(high_bust_to_bust_rows)} rows and adjust your stitch count to {int(bust_sts)} stitches. 
        You have knit to the bust. 
    """
        pattern += incr_1
    else: 
        incr_1 = f"""
        Knit in the round for {int(high_bust_to_bust_rows)} rows. 
        You have knit to the bust.
    """
        pattern += incr_1
    
    # Bust to Waist
    if waist_decr != 0:
        waist_decr_interval = bust_to_waist_rows / (waist_decr/4)
        decr_1 = f"""
        * Then, knit in the round for {int(waist_decr_interval - 1)} rows.
        On the next row, K1, SSK, then K until 3 stitches before the stitch marker, K2TOG, K2, SSK, then K until 3 before the stitch marker. K2TOG, K1. *
        Repeat the steps between the * * until you have {int(high_bust_to_bust_rows + bust_to_waist_rows)} rows, and adjust your stitch count to {int(waist_sts)} stitches.
        You have knit to the waist
    """
        pattern += decr_1
    else:
        decr_1 = f"""
        Knit in the round until you have {int(high_bust_to_bust_rows + bust_to_waist_rows)} rows. 
        You have knit to the waist.
    """
        pattern += decr_1

    # Waist to Hip
    if hip_incr !=0:
        hip_incr_interval = waist_to_hip_rows / (hip_incr/4)
        incr_2 = f"""
        * Knit for {int(hip_incr_interval - 1)} rows.
        On the next row, K1, SSK, then K until 3 stitches before the stitch marker, K2TOG, K2, SSK, then K until 3 before the stitch marker. K2TOG, K1. *
        Repeat the steps in between the * * until you have {int(high_bust_to_bust_rows + bust_to_waist_rows + waist_to_hip_rows)} rows, or until it reaches the desired length.
        You should have around {int(hip_sts)} stitches 
        You have knit to the hip.
        """
        pattern += incr_2
    else:
        incr_2 = f"""
        Knit in the round until you have {int(high_bust_to_bust_row + bust_to_waist_rows + waist_to_hip_rows)} rows.
        You have knit to the hip.
         """
        pattern += incr_2

    # Bind off
    pattern += f"""
        Bind off all stitches and weave in all ends.
        """


    print(pattern)

tube_top_pattern()

'''    
    pattern = f"""
    Top-Down Tube Top Pattern:
    1. Cast on {int(high_bust_sts) + 1} stitches for the high bust, placing a stitch marker after the {stitch_marker} cast on stitch.
    2. Join in the round and place a stitch marker. You should now have {int(high_bust_sts)} stitches. 
    3. Knit in the round for {int(bust_incr_interval - 1)} rows.
    4. On the {add_suffix(int(bust_incr_interval))} row, K1, M1L, then K until 1 stitch before the stitch marker, M1R, K2, M1L, then K until 1 stitch before the stitch marker and M1R.
    5. Repeat steps 3 and 4 until you have knit {int(high_bust_to_bust_rows)} rows and adjust your stitch count to {int(bust_sts)} stitches.
    6. Then, knit in the round for {int(waist_decr_interval - 1)} rows.
    7. On the next row, K1, SSK, then K until 3 stitches before the stitch marker, K2TOG, K2, SSK, then K until 3 before the stitch marker. K2TOG, K1.
    8. Repeat steps 6 and 7 until you have {int(high_bust_to_bust_rows + bust_to_waist_rows)}, and adjust your stitch count to {int(waist_sts)} stitches.
    9. Knit for {int(waist_to_hip_rows - 1)} rows.
    10. On the next row, K1, SSK, then K until 3 stitches before the stitch marker, K2TOG, K2, SSK, then K until 3 before the stitch marker. K2TOG, K1.
    11. Repeat steps 9 and 10 until you have {int(high_bust_to_bust_rows + bust_to_waist_rows + waist_to_hip_rows)} rows, or until it reaches the desired length.
    8. Bind off all stitches and weave in all ends.
    """
    print(pattern)
'''