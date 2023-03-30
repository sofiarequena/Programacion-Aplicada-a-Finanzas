class My_array:
    def __init__(self, elems, r, c, by_row ):
        self.elems = elems
        self.r = r
        self.c = c
        self.by_row = by_row
        
    
    def get_pos(self, j, k):
        '''
        

        Parameters
        ----------
        j : INT
            Numero de fila.Se empieza a contar desde 0.
        k : INT
            Numero de columna. Se empieza a contar desde 0.

        Returns
        -------
        m : INT
            Esta es la posicion en la lista elems de las coordenadas.

        '''
        if len(self.elems) == self.r*self.c:
            if self.by_row:
                m = j * self.c + k
            else:
                m = k * self.r + j
            
            return m
        
    def get_coords(self, position):
        '''
        

        Parameters
        ----------
        position : INT
            Es la posicin en la lista que queremos convertir a coordenadas.

        Returns
        -------
        j : INT
            Numero de fila, empieza a contar desde cero.
        k : INT
            Numero de columna, empieza a contar desde cero.

        '''
        if len(self.elems)==self.r*self.c:
            if self.by_row:
                j = position // self.c
                k = position % self.c
            else:
                k = position // self.r
                j = position % self.r
            
            return j, k
        
    def switch(self):
        '''
        Esta funcion cambia la forma de lectura de la matriz, para esto cambia el valor del atributo by_row.

        Returns
        -------
        None.

        '''
        newelms = []
        if self.by_row == True:
            for i in range(0,self.c):
                for j in range(0,len(self.elems), self.c):
                    newelms.append(self.elems[i+j])
                    self.by_row = False
        else:
            for i in range(0, self.r):
                for j in range(0, len(self.elems), self.r):
                    newelms.append(self.elems[i+j])
                    self.by_row = True
        self.elems = My_array(newelms, self.c, self.r, not self.by_row).elems
        
          
    def get_row(self,j):
        '''
        Esta funcion devuelve la fila j indicada

        Parameters
        ----------
        j : INT
           Fila que se quiere obtener, empieza a contar desde 1.

        Returns
        -------
        row : list
            lista con los valores de la fila j.

        '''
        row = []
        if self.by_row== True:
            row = self.elems[self.c*(j-1): self.c*(j-1)+ self.c] #usar slicing
        else:
            row = self.elems[j-1::self.c]
        return row
    
    
    def get_col(self, k):
        '''
        Esta funcion te devuelve la columna k indicada

        Parameters
        ----------
        k : int
            Numero de la columna que queremos obtener.Empieza a contar desde 1.

        Returns
        -------
        A : list
            La columna k indicada.

        '''
        if k in range(1, self.c + 1):
            A = My_array(self.elems, self.r, self.c, self.by_row).transpose().get_row(k)
        else:
            A = None
        return A
    

    def get_elem(self, j, k):
        if j in range(self.r) and k in range(self.c):
            A = self.elems[self.get_pos(j, k)]
        else:
            A = None
        return A
    
    def del_row(self, j):
        if self.r > 1:
            for i in range(self.c):
                self.elems.pop(j*self.c)
            self.r -= 1
        elif self.r == 1:
            self.elems = []
            self.r = 0
            self.c = 0
    
    def del_col(self, k):
        '''
        

        Parameters
        ----------
        k : int
            El numero de la columna a eliminar. Empieza a contar desde 1.

        Returns
        -------
        En esta funcion usas dos sets y le decis que saque la diferencia del uno del otro.

        '''
        self.elems = list(set(self.elems).difference(set(self.get_col(k))))
        return self.elems

    def swap_rows(self, j, k):
        if j in range(self.r) and k in range(self.r):
            for i in range(self.c):
                self.elems[j*self.c + i], self.elems[k*self.c + i] = self.elems[k*self.c + i], self.elems[j*self.c + i]
        else:
            print("Error")
         
    def swap_cols(self, l, m):
        if l in range(self.c) and m in range(self.c):
            for i in range(self.r):
                self.elems[i*self.c + l], self.elems[i*self.c + m] = self.elems[i*self.c + m], self.elems[i*self.c + l]
        else:
            print("Error")
        
    def scale_row(self, j, x):
        newlist = []
        for i in range(len(self.elems)):
            if self.by_row:
                if i == j * self.c:
                    for k in range(self.c):
                        newlist.append(self.elems[j*self.c + k] * x)
            else:
                if i == j:
                    for k in range(self.r):
                        newlist.append(self.elems[j + k*self.r] * x)
        for i in range(self.r):
            if i > j:
                for k in self.get_row(i+1):
                    newlist.append(k)
            elif i < j:
                for k in sorted(self.get_row(i+1), reverse=True):
                    newlist.insert(i,k)

        return My_array(newlist, self.r, self.c, self.by_row)
    

    def scale_col(self, k, y):
        return self.transpose().scale_row(k,y).transpose()
    
    def transpose(self):
        newelms = []
        if self.by_row == True:
            for i in range(0,self.c):
                for j in range(0,len(self.elems), self.c):
                    newelms.append(self.elems[i+j])
                    self.by_row = False
        else:
            for i in range(0, self.r):
                for j in range(0, len(self.elems), self.r):
                    newelms.append(self.elems[i+j])
                    self.by_row = True
        y = My_array(newelms, self.c, self.r, not self.by_row)
        return y
    
  
    
    def flip_cols(self):
        newelms = []
        for i in range(self.r):
            for j in range(self.c):
                newelms.append(self.elems[i*self.c + self.c - j - 1])
        return My_array(newelms, self.r, self.c, self.by_row)

    def flip_rows(self):
        newelms = []
        for i in range(self.r):
            for j in range(self.c):
                newelms.append(self.elems[(self.r - i - 1)*self.c + j])
        return My_array(newelms, self.r, self.c, self.by_row)
    
    def submatrix(self, i, j):
        newelms = []
        for k in range(self.r):
            if k != i:
                for l in range(self.c):
                    if l != j:
                        newelms.append(self.elems[k*self.c + l])
        return My_array(newelms, self.r - 1, self.c - 1, self.by_row)

    def det(self):
        determinante: float
        if self.r == self.c:
            if self.r == 1:
                determinante = self.elems[0]
            elif self.r == 2:
                determinante = self.elems[0]*self.elems[3] - self.elems[1]*self.elems[2]
            elif self.r > 2:
                determinante = 0
                bandera = 1
                for i in range(self.c):
                    submatrix = self.submatrix(0,i)
                    subdet = submatrix.det()
                    determinante += self.elems[i] * subdet * bandera
                    bandera *= -1
        return determinante
    
    def add(self, B):
        A = My_array([], 0, 0, self.by_row)
        if type(B) == My_array:
            if self.r == B.r and self.c == B.c:
                newlist = []
                for i in range(len(self.elems)):
                    newlist.append(self.elems[i] + B.elems[i])
                A = My_array(newlist, self.r, self.c, self.by_row)
            else:
                print("Error")
        elif type(B) == list or type(B) == tuple:
            if self.r == len(B) and self.c == len(B[0]):
                newlist = []
                for i in range(len(self.elems)):
                    newlist.append(self.elems[i] + B[i//self.c][i%self.c])
                A = My_array(newlist, self.r, self.c, self.by_row)
            else:
                print("Error")
        else:
            newlist = []
            for i in range(len(self.elems)):
                    newlist.append(self.elems[i] + B)
            A = My_array(newlist, self.r, self.c, self.by_row)
        return A
            
    def sub(self, B):
        A = My_array([], 0, 0, self.by_row)
        if type(B) == My_array:
            if self.r == B.r and self.c == B.c:
                newlist = []
                for i in range(len(self.elems)):
                    newlist.append(self.elems[i] - B.elems[i])
                A = My_array(newlist, self.r, self.c, self.by_row)
            else:
                print("Error")
        elif type(B) == list or type(B) == tuple:
            if self.r == len(B) and self.c == len(B[0]):
                newlist = []
                for i in range(len(self.elems)):
                    newlist.append(self.elems[i] - B[i//self.c][i%self.c])
                A = My_array(newlist, self.r, self.c, self.by_row)
            else:
                print("Error")
        else:
            newlist = []
            for i in range(len(self.elems)):
                    newlist.append(self.elems[i] - B)
            A = My_array(newlist, self.r, self.c, self.by_row)
        return A
    
    def rprod(self, B):
        A = My_array([], 0, 0, self.by_row)
        if type(B) == My_array:
            if self.c == B.r:
                newlist = []
                for i in range(self.r):
                    for j in range(B.c):
                        sum = 0
                        for k in range(self.c):
                            sum += self.elems[i*self.c + k] * B.elems[k*B.c + j]
                        newlist.append(sum)
                A = My_array(newlist, self.r, B.c, self.by_row)
            else:
                print("Error")
        elif type(B) == list or type(B) == tuple:
            if self.c == len(B):
                newlist = []
                for i in range(self.r):
                    for j in range(len(B[0])):
                        sum = 0
                        for k in range(self.c):
                            sum += self.elems[i*self.c + k] * B[k][j]
                        newlist.append(sum)
                A = My_array(newlist, self.r, len(B[0]), self.by_row)
            else:
                print("Error")
        else:
            print("Error")
        return A
    
    def lprod(self, B):
        A = My_array([], 0, 0, self.by_row)
        if type(B) == My_array:
            if self.r == B.c:
                newlist = []
                for i in range(B.r):
                    for j in range(self.c):
                        sum = 0
                        for k in range(self.r):
                            sum += B.elems[i*B.c + k] * self.elems[k*self.c + j]
                        newlist.append(sum)
                A = My_array(newlist, B.r, self.c, self.by_row)
            else:
                print("Error")
        elif type(B) == list or type(B) == tuple:
            if self.r == len(B[0]):
                newlist = []
                for i in range(len(B)):
                    for j in range(self.c):
                        sum = 0
                        for k in range(self.r):
                            sum += B[i][k] * self.elems[k*self.c + j]
                        newlist.append(sum)
                A = My_array(newlist, len(B), self.c, self.by_row)
            else:
                print("Error")
        else:
            print("Error")
        return A
    
    def generador_matriz_identidad(self, r, c):
        newlist = []
        for i in range(r):
            for j in range(c):
                if i == j:
                    newlist.append(1)
                else:
                    newlist.append(0)
        return My_array(newlist, r, c, self.by_row)
    
    def pow(self, n):
        if self.r == self.c:
            A = self.generador_matriz_identidad(self.r, self.c)
            for i in range(n):
                A = A.rprod(self)
            return A
        else:
            print("Error")

    


#Aca dejo hechas las invocaciones de cada cosa             
matrix = My_array([1,2,3,4], 2, 2, True)
#m = matrix.get_pos(1,0)
# cord = matrix.get_coords(5)
# swiss = matrix.switch()
# #My_array(swiss,3,2)
# print(swiss)

#w = matrix.pow(3)  
#print(w)  
# print(m)

#matrix = My_array([1,2,3,4], 2, 2, True)

# print(matrix.get_pos(1,2))
# print(matrix.get_coords(5))
#print(matrix.switch().elems)
#print(matrix.switch().switch())
# print(matrix.get_row(2))
#print(matrix.get_col(1))
# print(matrix.get_elem(1,2))

# matrix.del_col(3)
# print(matrix.elems)

# matrix.swap_cols(0,1)
# print(matrix.elems)

# print(matrix.scale_col(0,2).elems)

# print(matrix.flip_cols().elems)

# print(matrix.add([[1,2,3],[4,5,6]]).elems)

# print(matrix.generador_matriz_identidad(3,3).elems)

# print(matrix.pow(2).elems)

#print(matrix.get_col(1))

#print(matrix.del_col(1))
