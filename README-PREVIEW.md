# Miriã Cotrim Bridal Beauty — Concept Preview v1

Prévia demonstrativa baseada no documento e nas 54 imagens fornecidas. As dez páginas são estáticas, com componentes reutilizáveis em JavaScript e CSS responsivo. Nenhum backend, pagamento ou envio de formulário é executado.

## Executar

Na pasta deste projeto, execute `node prepare.mjs` e sirva `dist` com `python -m http.server 4173 --directory dist`. Abra `http://localhost:4173`. O comando de preparação atualiza os arquivos de entrada das dez rotas. Não é necessário instalar dependências.

## Conteúdo

`dist/siteContent.js` centraliza marca, contatos, serviços, portfólio, cursos, categorias de produtos, agendamento e textos EN/PT. Textos têm formato `English|Português`. `dist/uiContent.js` centraliza os demais textos de interface. A biografia é provisória (`bioPendingApproval`) e precisa ser aprovada pela Miriã. Localização comercial, e-mail, TikTok e Pinterest permanecem não informados; não são exibidos links fictícios.

## Fotos

As fotos originais estão identificadas em `asset-manifest.json`. As versões WebP e miniaturas ficam em `dist/images`. O logo é `01.webp`, a imagem principal é `44.webp` e o retrato da Miriã é `07.webp`. Nenhum rosto foi alterado. As categorias do portfólio são editáveis em `siteContent.js`.

## Contatos

Altere `contact.WHATSAPP_NUMBER` (apenas números com código do país) e `socialMedia` em `siteContent.js`. Os links de WhatsApp, Instagram e Facebook usam os contatos fornecidos. O WhatsApp abre uma conversa; não envia a mensagem automaticamente.

## Demonstrações e privacidade

Agendamento, proposta bridal, Academy, guia e newsletter validam campos e apresentam confirmação explícita de demonstração. Não enviam nem armazenam dados pessoais. A preferência de idioma é mantida em sessionStorage. A sacola guarda somente exemplos em memória até sair da página. Não há preços, compras ou reservas reais. Depoimentos e artigos são identificados como conteúdo futuro. As políticas do rodapé descrevem somente esta demonstração; precisam ser substituídas por textos aprovados antes de uso comercial. As fontes são carregadas de Google Fonts com fallback local.

## Integrações futuras

Substitua o manipulador do formulário de agendamento por uma integração oficial com Calendly, Cal.com ou Square Appointments. Consulte disponibilidade real no servidor, com fuso horário explícito, e só confirme após resposta bem-sucedida. Para Google Calendar, utilize OAuth no servidor e validação de conflitos. Nenhuma chave deve ir para os arquivos públicos.

Os formulários têm identificadores independentes (`inquiry`, `academy-list`, `guide`, `newsletter`) para conexão futura com um CRM ou provedor de e-mail. Implemente consentimento apropriado, validação no servidor e tratamento de falhas antes de ativar envios.

Os produtos têm estrutura futura documentada em `dist/product-schema.json`. Para Stripe ou Square, criar checkout no servidor, validar preços/estoque no servidor e confirmar pagamento com webhooks. A demonstração não aceita pagamentos.

## Pendências comerciais

Aprovar biografia e serviços; confirmar localização/e-mail; fornecer catálogo, preços e políticas; aprovar guia e artigos; fornecer depoimentos autorizados; conectar calendário, CRM e pagamentos quando necessário. Esta é uma prévia conceitual, não a versão comercial final.

## Vídeo da abertura

`dist/videoContent.js` configura vídeo, capa, controles e créditos. `dist/video/hero-desktop.mp4` é uma montagem silenciosa de 19,6 segundos, Full HD 1920×1080, H.264, 24 fps. `hero-mobile.mp4` é a versão vertical leve, 720×960. As fontes são cinco clipes Pexels (licença em https://www.pexels.com/license/), listados no botão de créditos do hero. As cenas são de inspiração e não representam clientes da Miriã. O clipe de arquitetura é identificado com tags de Flórida/Miami/Palm Beach; não foi confirmado como local de eventos. Os demais locais não foram confirmados como Flórida.

O hero respeita preferência de movimento reduzido e economia de dados, tem pausa/reprodução, capa estática e pausa fora da área visível. Não há áudio. Para trocar, mantenha os nomes dos arquivos ou altere a configuração. Os scripts `make_hero.py` e `optimize_video.py` documentam a edição; exigem FFmpeg via imageio-ffmpeg e os originais obtidos nas fontes. As fontes originais e ferramentas de edição ficam fora do pacote publicado.
