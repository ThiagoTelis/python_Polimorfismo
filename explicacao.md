Explicação do Polimorfismo neste Código
O termo polimorfismo significa "muitas formas". Em Python, isso acontece de forma natural devido à tipagem dinâmica e à herança, permitindo que diferentes classes respondam à mesma chamada de método de maneiras específicas.

Herança e Interface Comum:
As classes DiaDosNamorados, Natal e Aniversario herdam da classe base CartaoWeb. O uso do módulo abc (Abstract Base Classes) garante que todas as subclasses precisem obrigatoriamente implementar o método show_message. Isso cria um contrato uniforme: qualquer objeto do tipo CartaoWeb saberá responder ao comando show_message().

Sobrescrita de Métodos:
Embora todas compartilhem o mesmo nome de método (show_message), cada classe filha fornece a sua própria lógica e mensagem personalizada para a data comemorativa correspondente.

Execução Polimórfica (Duck Typing / Dynamic Dispatch):
No laço for, a variável cartao assume diferentes formas em cada iteração (ora é um objeto DiaDosNamorados, ora Natal, etc.). Quando chamamos cartao.show_message(), o Python não se importa estritamente com o tipo da variável, mas sim com o fato de o objeto possuir aquele método. Em tempo de execução, ele executa a versão exata do método pertencente àquele objeto específico.