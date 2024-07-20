test_str = "chia seed"
ans=min(test_str,key=lambda i: test_str.count(i))
print(ans)