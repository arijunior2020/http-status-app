from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Habilita o CORS para permitir requisições do frontend

STATUS_CODES = [
    # 1xx Informacional
    {"code": 100, "name": "Continue", "description": "O servidor recebeu a solicitação inicial e o cliente pode continuar."},
    {"code": 101, "name": "Switching Protocols", "description": "O servidor está mudando os protocolos conforme solicitado pelo cliente."},
    {"code": 102, "name": "Processing", "description": "O servidor está processando a solicitação, mas ainda não há resposta disponível."},
    {"code": 103, "name": "Early Hints", "description": "Indica que o cliente pode começar a carregar recursos enquanto o servidor prepara a resposta."},

    # 2xx Sucesso
    {"code": 200, "name": "OK", "description": "A solicitação foi bem-sucedida."},
    {"code": 201, "name": "Created", "description": "O recurso foi criado com sucesso no servidor."},
    {"code": 202, "name": "Accepted", "description": "A solicitação foi aceita para processamento, mas ainda não concluída."},
    {"code": 203, "name": "Non-Authoritative Information", "description": "A resposta foi modificada por um proxy intermediário."},
    {"code": 204, "name": "No Content", "description": "A solicitação foi bem-sucedida, mas não há conteúdo para retornar."},
    {"code": 205, "name": "Reset Content", "description": "Solicita ao cliente que reinicie o documento visualizado."},
    {"code": 206, "name": "Partial Content", "description": "A solicitação foi bem-sucedida e o servidor está entregando parte do conteúdo."},
    {"code": 207, "name": "Multi-Status", "description": "Fornece várias respostas de status (usado no WebDAV)."},
    {"code": 208, "name": "Already Reported", "description": "Elementos já foram listados em outra resposta (usado no WebDAV)."},
    {"code": 226, "name": "IM Used", "description": "O servidor executou uma resposta delta bem-sucedida."},

    # 3xx Redirecionamento
    {"code": 300, "name": "Multiple Choices", "description": "Há várias opções que o cliente pode seguir."},
    {"code": 301, "name": "Moved Permanently", "description": "O recurso foi movido permanentemente para outra URL."},
    {"code": 302, "name": "Found", "description": "O recurso foi encontrado em outra URL temporariamente."},
    {"code": 303, "name": "See Other", "description": "O cliente deve buscar o recurso em outra URL."},
    {"code": 304, "name": "Not Modified", "description": "O recurso não foi modificado desde a última solicitação."},
    {"code": 305, "name": "Use Proxy", "description": "O cliente deve acessar o recurso por meio de um proxy."},
    {"code": 306, "name": "Switch Proxy", "description": "Código não utilizado atualmente, reservado para mudanças de proxy."},
    {"code": 307, "name": "Temporary Redirect", "description": "Redirecionamento temporário para outra URL."},
    {"code": 308, "name": "Permanent Redirect", "description": "Redirecionamento permanente para outra URL."},

    # 4xx Erros do Cliente
    {"code": 400, "name": "Bad Request", "description": "O servidor não conseguiu entender a solicitação devido a uma sintaxe inválida."},
    {"code": 401, "name": "Unauthorized", "description": "Autenticação é necessária para acessar o recurso."},
    {"code": 402, "name": "Payment Required", "description": "Pagamento é necessário para acessar o recurso (experimental)."},
    {"code": 403, "name": "Forbidden", "description": "O servidor entendeu a solicitação, mas se recusa a autorizá-la."},
    {"code": 404, "name": "Not Found", "description": "O recurso solicitado não foi encontrado no servidor."},
    {"code": 405, "name": "Method Not Allowed", "description": "O método HTTP utilizado não é permitido para este recurso."},
    {"code": 406, "name": "Not Acceptable", "description": "O recurso não é capaz de gerar uma resposta aceitável pelo cliente."},
    {"code": 407, "name": "Proxy Authentication Required", "description": "Autenticação no proxy é necessária."},
    {"code": 408, "name": "Request Timeout", "description": "O servidor demorou muito para receber a solicitação."},
    {"code": 409, "name": "Conflict", "description": "Conflito com o estado atual do recurso no servidor."},
    {"code": 410, "name": "Gone", "description": "O recurso não está mais disponível e não há endereço alternativo."},
    {"code": 411, "name": "Length Required", "description": "O cabeçalho 'Content-Length' é necessário."},
    {"code": 412, "name": "Precondition Failed", "description": "Uma pré-condição na solicitação falhou."},
    {"code": 413, "name": "Payload Too Large", "description": "A carga de dados enviada é maior do que o servidor pode processar."},
    {"code": 414, "name": "URI Too Long", "description": "O URI solicitado é muito longo para o servidor processar."},
    {"code": 415, "name": "Unsupported Media Type", "description": "O tipo de mídia da solicitação não é suportado."},
    {"code": 416, "name": "Range Not Satisfiable", "description": "O intervalo solicitado não pode ser satisfeito."},
    {"code": 417, "name": "Expectation Failed", "description": "O cabeçalho 'Expect' não pôde ser satisfeito pelo servidor."},
    {"code": 418, "name": "I'm a teapot", "description": "Sou um bule de chá (piada RFC 2324)."},
    {"code": 421, "name": "Misdirected Request", "description": "A solicitação foi direcionada para um servidor incorreto."},
    {"code": 422, "name": "Unprocessable Entity", "description": "A solicitação está semanticamente errada."},
    {"code": 423, "name": "Locked", "description": "O recurso está bloqueado."},
    {"code": 424, "name": "Failed Dependency", "description": "A solicitação falhou devido a uma dependência."},
    {"code": 425, "name": "Too Early", "description": "O servidor não está disposto a processar a solicitação ainda."},
    {"code": 426, "name": "Upgrade Required", "description": "O cliente deve mudar para outro protocolo."},
    {"code": 428, "name": "Precondition Required", "description": "O servidor exige condições para a solicitação."},
    {"code": 429, "name": "Too Many Requests", "description": "O cliente enviou muitas solicitações em pouco tempo."},
    {"code": 431, "name": "Request Header Fields Too Large", "description": "Os campos do cabeçalho são muito grandes."},
    {"code": 451, "name": "Unavailable For Legal Reasons", "description": "Indisponível por razões legais."},

    # 5xx Erros do Servidor
    {"code": 500, "name": "Internal Server Error", "description": "O servidor encontrou uma condição inesperada."},
    {"code": 501, "name": "Not Implemented", "description": "O servidor não suporta a funcionalidade necessária para atender à solicitação."},
    {"code": 502, "name": "Bad Gateway", "description": "O servidor recebeu uma resposta inválida de um servidor upstream."},
    {"code": 503, "name": "Service Unavailable", "description": "O servidor está temporariamente indisponível."},
    {"code": 504, "name": "Gateway Timeout", "description": "O servidor não recebeu uma resposta em tempo de um servidor upstream."},
    {"code": 505, "name": "HTTP Version Not Supported", "description": "A versão HTTP usada na solicitação não é suportada pelo servidor."},
    {"code": 506, "name": "Variant Also Negotiates", "description": "Erro de negociação de conteúdo."},
    {"code": 507, "name": "Insufficient Storage", "description": "O servidor não tem espaço suficiente para armazenar a solicitação."},
    {"code": 508, "name": "Loop Detected", "description": "Um loop infinito foi detectado."},
    {"code": 510, "name": "Not Extended", "description": "Extensões adicionais são necessárias para atender à solicitação."},
    {"code": 511, "name": "Network Authentication Required", "description": "A autenticação da rede é necessária."}
]

@app.route('/status', methods=['GET'])
def get_status_codes():
    return jsonify(STATUS_CODES)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
