from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('helvetica','B',20)
        self.cell(0,10,'Header',border=False,ln=1,align='C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica','I',10)
        self.cell(0,10,f'Page{self.page_no()}/{{nb}}',align='C')

    def output_table(self,result_data,no_of_column):
        self.add_page()
        self.alias_nb_pages()
        self.no_of_column = no_of_column
        self.result_data = result_data
        
        self.set_font('helvetica',size=8)
        col_width = self.epw/self.no_of_column    
        line_height = self.font_size * 12
        
        
        for row in self.l:
            for item in row:
               
               self.multi_cell(col_width, line_height, str(item), border=1, ln=3, max_line_height=self.font_size)
            self.ln(line_height) 
    
    def save_pdf(self,file_name):
        self.filename = file_name
        self.output(file_name)
        print('File Created Sucessfully')

    def withIndex(self,head,retirve_data):
        self.retirve_data = retirve_data
        self.head = head
        self.l =[]
        for i in self.retirve_data:
            self.l.append(i)
        index = self.l.index(self.l[0])
        self.l.insert(index,head)