class Model:
    def __init__(self):
        self.value=''
        self.operator=''
        self.previous=''
        self.current=''

    def calculate(self,caption):
        #print(f'Calculating for {caption}')
        if caption=='C':
            self.previous=''
            self.value=''
            self.operator=''

        elif isinstance(caption,int):
            self.value+=str(caption)
        
        elif caption=='+/-':
            self.value=self.value[1:] if self.value[0]=='-' else '-'+self.value
        
        elif caption=='%':
            value=float(self.value) if '.' in self.value else int(self.value)
            self.value=str(value/100)
        elif caption=='.':
            if not caption in self.value:
                self.value+=caption
        elif caption=='=':
            value=self._evaluate()
            if '.0' in str(value):
                value=int(value)
            self.value=str(value)

        else:
            if self.value:
                self.operator=caption
                self.previous=self.value
                self.value=''
        return self.value

    def _evaluate(self):
        return eval(self.previous+self.operator+self.value)    