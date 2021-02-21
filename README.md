## Programa que envia E-mails para contas no gmail.
___
### Observação:
*De momento nao quis fazer funções e classes separadas para cada possivel funcionalidade, porém desejo automatizar o processo de envio de emails, quando isso ocorrer pretendo adcionar os "def, class e se necessário modulos", para deixar o código mais limpo e reutilizavel*

**Mapa do código:** 

1. Este bloco solicita ao úsuario que infome seu email, a senha é guardada dentro de uma variável de ambiente no terminal('é obrigatório que você defina a senha em seu terminal'), Ex:```export VARIAVEL_DA_SENHA='senha'```

```Python
email_from = input('Infome o seu E-mail: ')
email_password = os.getenv('EMAIL_PASSWORD')
```
___

2. Este bloco questiona ao úsuario se ele deseja incluir novos destinátarios, se sim o ```while``` continha e solicita um novo email, se não o programa continua o seu fluxo

```Python
while True:
    receiver = input('Quais são os destinatarios ?: ')
    list_receivs = [receiver]

    reapt = input('\nAdcionar mais um destinatario?: ')
    if reapt == 's':
        continue
    else:
        break
``` 
____

3. Este bloco instância a função ```MIMEMultipart()```, ela sera responsável por montar a formatação do cabeçalho, contendo o email do remetente e titulo

```Python
header = MIMEMultipart()
header['From'] = email_from
header['Subject'] = title
```
___

4. Este bloco intância a função ```smtplib.SMTP```,ele sera responsável por definir qual será o servidor a ser usado e qual porta devera ser utilizada na conexão

```Python
email_server = 'smtp.gmail.com'
protocol_smtp = smtplib.SMTP(email_server, 587)
```
___

5. Este bloco faz a comunicação em si com o servidor de forma segura, é necessário inserir do contrario o servidor do gmail pode recusar a conexão.

```Python
protocol_smtp.ehlo()
protocol_smtp.starttls()
protocol_smtp.ehlo()
```
___

6. Neste ultimo fragmento, ele ira fazer o login no gmail, utilizando as variáveis definidas no inicio do programa ```email_from e email_password```, em seguida irá enviar a menssagem pré definida para a lista de destinatários e por fim encerrará a conexão com o servidor

```Python
protocol_smtp.login(email_from, email_password)
protocol_smtp.sendmail(email_from, ','.join(
list_receivs), header.as_string())
protocol_smtp.quit()
```