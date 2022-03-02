# Python Collections Parte 1 - Listas e Tuplas

Curso da Alura sobre listas e tuplas, suas diferenças e suas funções

## Objetivo Final &#x1F3AF;

Criar diferentes coleções de vários elementos

URL do curso -> [Python Collections Parte 1 - Listas e Tuplas](https://cursos.alura.com.br/course/python-collections-listas-e-tuplas)

![Python Collections Parte 1 - Listas e Tuplas](https://www.alura.com.br/assets/api/share/curso-python-collections-listas-e-tuplas.png)

## Links Úteis &#x1F517;
* [NumPy](https://numpy.org/) - Site para uma biblioteca de conjuntos.

## Siglas &#x1F5FA;
*

## Atalhos &#x2328;
*

## 01 - Listas e Operações &#x1F516;
* O que é coleção.
* Criar lista.
* Verificar o tipo da lista e o tamanho da lista.
* Mostrar na tela o valor conforme sua posição na lista.
* Alterar valores que estão dentro da lista.
* Adicionar valores no final da lista.
* Percorrer a lista.
* Remover elemento da lista.
* Remover **todos** elementos da lista.
* Verificar se o elemento está dentro da lista.
* Inserir um elemento na posição que desejamos.
* Utilizar um list comprehension.
* Fazer filtragens.
* Criar uma função e deixar um valor padrão.
* Quais são os problemas da mutabilidade.

### 01 - Introdução as Coleções e Listas
* `.append(ELEMENT)` para adicionar um elemento.
* `.remove(ELEMENT)` para remover um elemento.

### 02 - Mais Operações em Listas e List Comprehension
* `ELEMENT in LIST` para verificar se um elemento está dentro de uma lista.
* `.insert(INDEX, ELEMENT)` insere um elemento na posição especificada.
* `.extend(ITERABLE)` adiciona vários elementos de uma vez no final da lista.
* `[(OPERATION) for ELEMENT in LIST]` cria uma nova lista de acordo com a operação.
* `[ELEMENT for ELEMENT in LIST FILTER]` cria uma nova lista filtrando os elementos.

### 03 - Problemas da Mutabilidade da Lista
* Deixar valores padrão para uma função para evitar o problema da mutabilidade.

## 02 - Tuplas &#x1F516;
* Criar uma classe e métodos.
* Criar uma lista de referência para objetos.
* Lidar com referências.
* O que é uma tupla.
* Fazer tupla de listas.
* Diferença entre programação orientada a objetos e funcional.
* Fazer uma lista de tuplas.

### 01- Listas com Objetos de Classes Nossas
* Referências do mesmo objeto em uma lista.

### 02 - Tuplas, Objetos e Anemia
* Usar uma **tupla** com `()`.

### 03 - Tupla de Objetos e Lista de Tuplas
* Diferenças entre as 2 abordagens.

## 03 - Polimorfismo e Arrays &#x1F516;
* Conceito de herança e polimorfismo.
* Herdar classe.
* O que é o duck typing.
* Fazer um array no Python.
* Fazer anotações.

### 01 - Listas e Polimorfismo
* Usando polimorfismo nos elementos das listas.

### 02 - Arrays e Numpy
* Usando a classe `array`.

### 03 - Método Abstrato
* Deixar a classe `Account` abstrata.

## 04 - Igualdade &#x1F516;
* Utilizar o `__eq__`.
* Utilizar boas práticas para comparação .
* Usar o `isinstance` para verificar se uma instância de um objeto.

### 01 - Igualdade e o `__eq__`
* Verificar igualdade com um objeto do tipo `SalaryAccount`.

## 05 - Outros Builtins &#x1F516;
* O que são `enumerated`.
* Como funciona a função `range`.
* Desempacotar tuplas.
* Utilizar a função `len`.

### 01 - Builtins como Enumerated, range e desempacotamento Automático de Tuplas
* Gerar listas com índices.
* Usar desempacotamento nas listas.

## 06 - Ordem Natural &#x1F516;
* Utilizar a função **sorted** para fazer a ordenação sem mudar o conteúdo na lista original.
* Usar a função **sort** para ordenar atribuindo e mudando a lista original.
* Utilizar a função **reversed** que ordena do maior para o menor sem alterar a lista original.

### 01 - Ordenação Básica
* Usar o `sorted()` para ordenar uma lista.
* Usar o `sorted(reverse=?)` para ordenar uma lista de forma decrescente ou não.

## 07 - Ordenação Customizada &#x1F516;
* O que é ordem natural.
* Ordenar e comparar objetos.
* Utilizar o `attrgette`.
* Usar o `__lt__`: menor que (less than) para comparações.

### 01 - Ordenação dos Objetos sem Ordem Natural
* Ordenar objetos através do `key=`.

### 02 - Implementando o `__it__`
* Implementar o próprio método de ordenação do objeto (`<`) com `__lt__`.