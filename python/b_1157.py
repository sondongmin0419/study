st = input().upper()

st_set = set(st)
max_count = 0
max_ch = ''

for i in st_set:
    if max_count < st.count(i):
        max_count = st.count(i)
        max_ch = i
    elif max_count == st.count(i):
        max_ch = '?'


print(max_ch)
