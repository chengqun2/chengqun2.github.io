# Convert multi-line string to list
data = """rec24QzHauQROwTZ3
recEdmaOxeqrtpb44
rec7BerHf3k7vKFCN
recEqGOpiIVpUiGY3
recr0zLg4m8DfMsdg
recMsTiFF9I0vcb5c
reciIbkepjzs4NO3l
rec1MQOCR8deNyIn5
recWgVMMr9WOUqNAw
recQSQJdSXo99Ccdy
recvLmh0YKHxqUY3x
recQBxk9gNYTJX6AJ
recaILrkbYrLqcem4
recFKfyiG3il7kO00
rec7lnzO3z8rhaFPz
recvInC6dO6otF4Zi
recAYxOcnmfFiHnZo
rec2qt0eR1xNjGb1d
recuQ7YJ54Fe3vODF
recox37SkhvvfJgR1
recy2aflKCMfGMwLU
recatwHxazC2HH8x9
recDLUDFmlj0nM921
recE21OiwspSb84uf
recykObZUaTZjhKQX
recp0nIjqEGbh7zKE
recCN10qFVHFRXWT8
recM1f2xQ37J1p5vI"""

array = [line.strip() for line in data.split('\n') if line.strip()]
print(array)
