# youtube-music-mobile-test

### Descrição

Este projeto contém o código responsável por realizar testes mobile do app [YouTube Music](https://play.google.com/store/apps/details?id=com.google.android.apps.youtube.music&hl=pt_BR&pli=1).

- [Appium](https://appium.io/docs/en/2.0/quickstart/install/)
- [Python](https://www.python.org/downloads/release/python-3120/)
- [Pytest](https://docs.pytest.org/en/stable/announce/release-8.3.2.html)

### Clone e Execução do projeto

Para clonar o projeto siga os seguintes passos:

No terminal:
```
git clone git@github.com:caldasmatheus/youtube-music-mobile-test.git
```

No contexto onde o projeto foi clonado:
```
cd youtube-music-mobile-test
```

Na raiz do projeto:
```
pip install -r requirements.txt
```

:exclamation: **Observação**: Para questões relacionadas a autenticação por SSH, consulte a documentação do GitHub em "[Crie e Adicione seu Par de Chaves SSH](https://docs.github.com/pt/authentication/connecting-to-github-with-ssh)".

### Tipos de Execução dos Testes

Para executar o projeto **youtube-music-mobile-test** siga as etapas:

* Inicie o Appium:

```
npx appium
```

* Exemplo de execução de todos os cenários de testes:

```
pytest tests
```

* Exemplo de execução de uma classe de teste específica:

```
pytest tests/test_CT001.py
```

* Exemplo de execução de um cenário de teste específico:

```
pytest tests/test_CT001.py::Test_CT001::test_create_playlist
```

### Contribuições

Para contribuir com o projeto, siga estas etapas:

1. Crie um *branch*: *`git checkout -b <branch_name>`*;
2. Faça suas alterações e confirme-as: *`git commit -m '<commit_message>'`*;
3. Envie a *branch* local para o repositório remoto: *`git push origin <branch_name>`*;
4. Crie o *pull request*.

:exclamation: **Observação**: Como alternativa, consulte a documentação do GitHub em "[Criando um Pull Request](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)".

### Contato

Em caso de dúvidas: <raimundo.matheus@dcx.ufpb.br>. :incoming_envelope:
