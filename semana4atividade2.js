public static void main(String[] args) {
    Conta c1 = new Conta();
    c1.titular = "Duke";
    c1.saldo = 227;

    Conta c2 = new Conta();
    c2.titular = "Duke";
    c2.saldo = 227;

    if (c1 == c2) {
        System.out.println("Contas iguais");
    }
}

class Conta {

    void transfere(Conta destino, double valor) {
        this.saldo = this.saldo - valor;
        destino.saldo = destino.saldo + valor;
    }
}