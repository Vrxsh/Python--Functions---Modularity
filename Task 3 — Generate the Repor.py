def generate_report(classified, passing_avg=70):
    print("===== Student Grade Report =====")
    
    passed = 0
    failed = 0
    
    for name, (avg, grade) in classified.items():
        status = "PASS" if avg >= passing_avg else "FAIL"
        if status == "PASS":
            passed += 1
        else:
            failed += 1
        print(f"{name:<7} | Avg: {avg:<5} | Grade: {grade} | Status: {status}")
    
    print("===============================")
    print(f"Total Students : {len(classified)}")
    print(f"Passed         : {passed}")
    print(f"Failed         : {failed}")
    
    return passed