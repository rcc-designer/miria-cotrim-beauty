# Miriã Cotrim Bridal Beauty

Site institucional e portfólio bilíngue (inglês/português), preparado para publicação pelo GitHub e Vercel.

## Publicar no GitHub

1. Crie um repositório vazio no GitHub. Não marque as opções para adicionar README, `.gitignore` ou licença.
2. Abra o terminal dentro desta pasta e execute:

```bash
git init
git add .
git commit -m "Versão inicial do site"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
git push -u origin main
```

Se o repositório já estiver criado e conectado, basta executar:

```bash
git add .
git commit -m "Atualiza site"
git push
```

## Publicar no Vercel

1. Acesse [vercel.com](https://vercel.com/) e entre com a conta do GitHub.
2. Selecione **Add New > Project**.
3. Importe o repositório criado no GitHub.
4. O arquivo `vercel.json` já define o comando de build e a pasta de saída.
5. Clique em **Deploy**.

Configuração esperada pelo Vercel:

- Framework Preset: `Other`
- Build Command: `npm run build`
- Output Directory: `dist`
- Install Command: pode ficar no padrão

Não são necessárias variáveis de ambiente para esta versão.

## Validar antes de publicar

É necessário ter o Node.js 18 ou superior instalado.

```bash
npm run build
npm run check
```

Para visualizar localmente, depois do build:

```bash
npx serve dist
```

## Onde alterar o conteúdo

- `dist/siteContent.js`: contatos, redes sociais, textos principais, serviços, portfólio, cursos e agendamento.
- `dist/uiContent.js`: textos da interface em inglês e português.
- `dist/images/`: imagens WebP e miniaturas.
- `dist/video/`: vídeo e capa da abertura.
- `dist/styles.css`, `dist/components.css` e `dist/video.css`: aparência do site.

Depois de qualquer alteração, execute `npm run build` e `npm run check` antes de enviar ao GitHub.

## Situação desta versão

Esta é uma demonstração funcional. Os formulários, o calendário, a loja e a newsletter ainda não enviam nem armazenam dados. Para uso comercial, eles deverão ser conectados aos serviços escolhidos pela profissional (por exemplo, Calendly/Cal.com, CRM e meio de pagamento).

As imagens de clientes e o material de marca devem permanecer sob autorização da proprietária. Não foi adicionada uma licença pública ao repositório.
