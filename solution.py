--------------------------------------------------------------------------------------------
#nannaku prematho puzzle solution
"""This will work only if initially killing starts with the second person"""

def nannakuprematho(n,k):
	if(k==2):
		a=1
		while a<=n:
			a*=2
		return (2*n)-a+1
	else:
		return print("sorry this code doesn't work other than 2")
			
		

if __name__=="__main__":
	n=int(input("enter no of persons: "))
	k=int(input("Enter which person dies first: "))
	print("The person who is alive is: ",nannakuprematho(n,k))
--------------------------------------------------------------------------------------------
sample output:
E:\Programming\HackerRank>python nannakuprematho.py
enter no of persons: 100
Enter which person dies first: 2
The person who is alive is:  73

E:\Programming\HackerRank>python nannakuprematho.py
enter no of persons: 1000
Enter which person dies first: 2
The person who is alive is:  977

E:\Programming\HackerRank>python nannakuprematho.py
enter no of persons: 100
Enter which person dies first: 3
sorry this code doesn't work other than 2
The person who is alive is:  None


