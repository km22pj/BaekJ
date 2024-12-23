st = input()
cro_list = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]
cnt = 0
length = len(st)
index = []
for ch in cro_list:
    if ch in st:
        length -= len(ch) * st.count(ch)
        cnt += st.count(ch)
        st = st.replace(ch, "*" * len(ch))
print(cnt + length)
