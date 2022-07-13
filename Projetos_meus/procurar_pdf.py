# -*- coding: utf-8 -*-
"""
Programa para procurar palavras em pdf's
Editor: Gabriel Augusto Lyra Porto
"""
#Built-in Python Libraries
import os
#import Process as pc

#3rd Parthy Libraries
import fitz

#Global Variables: full_path and pdf.

# do your work here

def pdf_location(
      directory):
    '''
    -> Iterate over the given directory and produces a list with the full
    path to all the files. Other directories aren't iterateds.
    Futhermore produces a global list called 'pdf' that has the pdf names.

    Parameters
    ----------
    directory : STR. The path to the wanted directory.

    Returns
    -------
    full_path: A list with the full path to each of the pdf's.
    
Made by: Gabriel Augusto
    '''
    
#Show the archives in the selected directory
    global full_path
    global pdf
    global directory_path
    full_path=[]
    directory_path= directory[:]
    pdf=[]
    for nome in os.listdir(directory):
       
#Full name to PDF
        path_pdf=os.path.join(directory,nome)
        
#Checking if the file is a PDF
        if os.path.isfile(path_pdf):

#Adicionando o arquivo em uma lista para uso posterior
            pdf += [nome]
            full_path.append(path_pdf)
    return full_path



#entrando (hummmmmm) nas páginas do pdf
#ps.: página e documentos são dois objetos distintos nessa biblioteca 'fitz'

def pdf_word_getter(
        pdf_paths, keyword):
    '''
    -> This function gets a path o a pdf in the first argument and search for 
    the keyword given in the secund argument in the file. Then give a list na-
    med results.

    Parameters
    ----------
    x : LIST
        A list with the pdf's path.
    keyword : STR
        The keyword that you want to search in the .

    Returns
    -------
    results: LIST.
        A list with all the pdf's files that has the string put in the parame-
        ter keyword.

    '''
    global directory_name
    global results
    directory_name = keyword[:]
    results=[]
    text = str()
    for i in range(
            len(pdf_paths)):  
        for page in fitz.open(full_path[i], filetype='pdf'):
            text +=page.get_text()
            if keyword.upper() in text.upper():
                results.append(pdf[i])
                text=''
                break
    print()
    print('-'*40)
    print()
    return results and print(f'A lista de todos os arquivos que possuem a palavra-chave - {keyword} - é: {results}')


def directory_creation(directory, new_dir_name):
    '''
    

    Parameters
    ----------
     : TYPE, optional
        DESCRIPTION. The name of .
    dir_name : TYPE, optional
        DESCRIPTION. The default is directory_name.

    Returns
    -------
    None.

    '''
    
    global a
    a = new_dir_name[:]
    os.chdir(directory)
    try:
        os.mkdir(new_dir_name)
    except:
        print('\n')
        print('-='*40)
        print(f'O diretório com nome - {new_dir_name} - já existe, movendo para dentro dessa pasta.')
        



def txt_creator(
      txt_name = 'resultado_palavra_chave'):
    
    
    os.chdir(a)
    f = open(txt_name,'w+')
    f.write('Os resultados da busca são: ')
    f.write('\n')
    for i in results:
        f.write(i)
        f.write('\n')
    f.close()
    os.chdir(directory_path)
    
    
a = 0


