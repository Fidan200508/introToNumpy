import numpy as np
array=np.array([1,2,3,4,5])
print(array)
print("Olcu: ")
print(array.shape)  #number of elements in array

array2=np.array([[1,2,3],[4,5,6]])
print(array2)
print("Olcu: ")
print(array2.shape)   #number of rows/number of columns

arr_zeros=np.zeros((3,3))   #tuple-> row.column
arr_ones=np.zeros((2,3))
arr_arange=np.arange(2,10,3)
arr_random=np.random.rand(2,2)
print(arr_zeros)
print(arr_ones)
print(arr_arange)
print(arr_random)

a=np.array([1,2,3])
b=np.array([4,5,6])
cem=a+b
hasil=a*b
print("Cem",cem)
print("Hasil",hasil)
print("Dot product",np.dot(a,b))
print("Sinus",np.sin(a))
print("Exponent",np.exp(a))
print("Square root",np.sqrt(a))
#NumPy array np.array([1,2,3])  ->element-wise operations are supported(addition and multiplication)  .dtype, .shape work
#Python list [1,2,3] ->Multiplication only works with integers   .dtype, .shape don't work
#python tuple (1,2,3) ->Immutable sequence Tuples cannot be added or multiplied element-wise either. it can concatenates(T+t=2,4,2,4) or repeat(2,3,2,3,2,3)


'''
array1=np.array([1,2,3,4])
array2=np.array(2,3,4)  #linear algebrada dot product qaydalari burda da kecerlidir.
print(np.dot(array1,array2))
'''

'''array1=np.array([1,2,3,4],[2,3,4])
array2=np.array([5,6,7])
print(np.dot(array1,array2))  #linear algebrada neceki coxolculu massivleri dot product la vura bilmirik, burda da hemcinin.
'''

# arr[i]	ith row
# arr[:, j]	jth column (all rows)
# arr[i, j]	single element at row i, column j
# arr[start:end, start:end]	sub-array from slice of rows and columns

#Boolean indexing
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("First row: ",a[0]) #first row
print("First column: ",a[:,0]) #all rows->first column
print("Last row: ",a[:-1])
print("Middle element: ",a[1,1]) #middle element
print("Sub-array: ",a[: 2,1:] )
print("Elements: ",a[a>5])

arr=np.arange(1,10) #funksiyası ilə 1-dən 9-a qədər ədədlərdən ibarət array yaradılır.
print(arr)
reshaped=arr.reshape(3,3)  #array 3x3 ölçülü kvadrat formaya salınır
print(reshaped)
flattened=reshaped.flatten()#array yenidən 1 ölçülü formaya gətirilir
print(flattened)
transposed=reshaped.T
print(transposed)  #arrayin transpozu alınır, yəni sətir və sütunlar yer dəyişir.

data=np.random.randint(1,100,size=(5,5))
print(data)
print("Sum is: ",np.sum(data))
print("Mean is: ",np.mean(data))
print("Std is: ",np.std(data))
print("Median is: ",np.median(data))
print("Max is: ",np.max(data))
print("Min is: ",np.min(data))
print("Sum of columns is: ",np.sum(data, axis=0)) #axis=0->column
print("Mean of rows is: ",np.mean(data,axis=1)) #axis=1->row

#NumPy treats vector as a row repeated for each row of arr
#The shapes (3,3) and (3,) are compatible for broadcasting->column numbers and vector column should be same
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
vector=np.array([1,2,3])
result=arr+vector
print(result)

#Fancy Indexing
array=np.array([0,10,20,30,40,50])
indices=[0,2,4]
print("fancy indexing: ",array[indices])

#Maskalama ve deyisdirme
arr=np.array([10,20,30,40,50])
arr[arr<30]=0
print("New array: ",arr)

a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
vstacked=np.vstack((a,b))
print("Verrtical stack: ",vstacked)
hstacked=np.hstack((a,b))
print("Horizontal stack: ",hstacked)
splitted=np.split(hstacked,2,axis=0) #along columns
print("Splitted: ",splitted[0],"\n",splitted[1])


#Determinant
matrix=np.array([[1,2],[4,5]])
det=np.linalg.det(matrix) #determinant
print("Determinant: ",det)
inverse=np.linalg.inv(matrix) #matriksin əksi(inversi)
print("Inverse: ",inverse)
#Əgər determinant sıfır deyilsə, matriksin tərsi mövcuddur.

# argmax() funksiyası arraydəki ən böyük elementin indeksini tapır.
# argmin() funksiyası isə ən kiçik elementin indeksini tapır.
# İndeks massivdə elementlərin sırasını göstərir, 0-dan başlayır.
# Bu funksiyalar massivdə maksimum və minimum dəyərlərin yerini tapmaq üçün faydalıdır.
arr=np.array([1,5,8,10,3])
print("Max value's index is: ",arr.argmax())
print("Min value's index is: ",arr.argmin())

#unikal elementler ve siralama
array=([1,5,3,3,1,9])
print("Sorting array: ",np.sort(array))
print("Unique elements: ",np.unique(array))

array=np.array([3,6,10,15,24,45])
clipped=np.clip(array,10,30) # Clip: 10-dan kiçikləri 10, 30-dan böyük olanları 30 edir
print(clipped)
result=np.where(array>15,"Boyukdur","Kicik ve beraberdir.") # Where: şərtə görə seçim
print(result)


#arr adlı arraydə np.nan dəyərləri — yəni boş və ya naməlum ədədlər — yerləşdirilir.
# np.isnan(arr) funksiyası ilə arraydə NaN (Not a Number) dəyərlərin olub-olmadığı yoxlanılır.
# np.nan_to_num(arr, nan=0) funksiyası ilə bütün NaN-lar 0 ilə əvəz olunur.
# Bu üsul verilənlərdə boşluqları təmizləmək və hesablamalara hazır hala gətirmək üçün istifadə olunur.
# Nəticədə təmizlənmiş array alınır
arr=np.array([1, np.nan, 6,np.nan,30])
print("NaN varmi? :", np.isnan(arr) )
cleaned=np.nan_to_num(arr, nan=0)
print("Cleaned version: ", cleaned)

# np.random.seed(42) funksiyası, hər dəfə eyni təsadüfi nəticələrin alınması üçün istifadə olunur.
# Bu, təkrar istehsal edilə bilən nəticələr əldə etmək üçün vacibdir, xüsusilə test və analiz məqsədləri ilə.
# Daha sonra np.random.randint(1, 100, 5) ilə 1-dən 100-ə qədər (100 daxil deyil) 5 ədəd təsadüfi tam ədəd yaradılır.
# Seed təyin olunduğu üçün bu ədədlər hər çalışmada eyni olacaq.
np.random.seed(42)
print("Random numbers: ",np.random.randint(1,100,5))



