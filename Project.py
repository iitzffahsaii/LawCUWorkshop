while True:
    income=int(input("Total income: "))
    income47=income-60000
    if income47>=250000:
        income42=income47-100000
        if income42==150000:
            tax=0
            print("Tax:",tax)
        elif income42>150000 and income42<=300000:
            income4=income42-150000
            tax=income4*0.05
            print("Tax:",tax)
        elif income42>300000 and income42<=500000:
            income4=income42-300000
            step1=income4*0.1
            tax=step1+7500
            print("Tax:",tax)
        elif income42>500000 and income42<=750000:
            income4=income42-500000
            step2=income4*0.15
            tax=step2+7500+20000
            print("Tax:",tax)
        elif income42>750000 and income42<=1000000:
            income4=income42-750000
            step3=income4*0.2
            tax=step3+7500+20000+37500
            print("Tax:",tax)
        elif income42>1000000 and income42<=2000000:
            income4=income42-1000000
            step4=income4*0.25
            tax=step4+7500+20000+37500+50000
            print("Tax:",tax)
        elif income42>2000000 and income42<=5000000:
            income4=income42-2000000
            step5=income4*0.3
            tax=step5+7500+20000+37500+50000+250000
            print("Tax:",tax)
        elif income42>5000000:
            income4=income42-5000000
            step6=income4*0.35
            tax=step6+7500+20000+37500+50000+250000+900000
            print("Tax:",tax)
    elif income47<250000:
        income42=income47-income47*0.4
        tax=0
        print("Tax:",tax)