import xlrd

wb = xlrd.open_workbook(filename=r"HKR.xlsx", encoding_override=True)
wb_len = len(wb.sheets())
# class ReadExcel():
user_case = []
save_case = []
take_case = []
transfor_case = []
def readdata(count):
    for j in range(wb_len):
        st = wb.sheet_by_index(j)
        rows = st.nrows
        # cols = st.ncols
        for i in range(1,rows):
            if j == 0:
                data = st.row_values(i)
                user_case.append([data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],i])
                # print(save_case)

            elif j == 1:
                data = st.row_values(i)
                save_case.append([data[0],data[1],data[2],i])

            elif j == 2:
                data = st.row_values(i)
                take_case.append([data[0],data[1],data[2],data[3],i])

            elif j == 3:
                data = st.row_values(i)
                transfor_case.append([data[0],data[1],data[2],data[3],data[4],i])


    if count == 0:
        return user_case
    elif count == 1:
        return save_case
    elif count == 2:
        return take_case
    elif count == 3:
        return transfor_case

# print(save_case)
# print(readdata(0))




