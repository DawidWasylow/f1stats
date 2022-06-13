// ---------------------------------------------------------------------------

# include <vcl.h>
# pragma hdrstop

# include "Unit1.h"
// ---------------------------------------------------------------------------
# pragma package(smart_init)
# pragma resource "*.dfm"


# define Sx 500
# define Sy 500
# define N 5
bool
spotkanie_owieczki(TImage * owca, TImage * wilk)
{
if (owca->Left >= wilk->Left-owca->Width & &
owca->Left <= wilk->Left+wilk->Width & &
owca->Top >= wilk->Top-owca->Height & &
owca->Top <= wilk->Top+wilk->Height)
{
return true;
}
else return false;

}

TForm1 * Form1;
// ---------------------------------------------------------------------------
__fastcall
TForm1::TForm1(TComponent * Owner)
: TForm(Owner)
{

}
// ---------------------------------------------------------------------------


class Zwierze // klasa abstrakcyjna


{
    public:
        int x0, y0, vx, vy;
int
masa, q;

virtual
void
ruch() = 0;

};

// KLASA
OWCA // // // // // // // // // // // // // // // // // // // //


class Owca: public


Zwierze
{
    public:
        TImage * ksz_o;
virtual
void
ruch()
{
    x0 += vx;
y0 += vy;
if (x0 >= Sx)
{vx = -vx;
x0 = Sx - 1;}
if (x0 < 0)   {vx=-vx; x0=0;}
if (y0 >= Sy) {vy=-vy; y0=Sy-1;}
if (y0 < 0)   {vy=-vy; y0=0;}
ksz_o->Left=x0;
ksz_o->Top=y0;
}
Owca(); // konstruktor owcy
~Owca(void); //
};

Owca::Owca() // konstruktor
owcy - stworzenie
ksztaltu
i
przypisanie
wartosci
poczatkowych
{
    x0 = random(Sx);
y0 = random(Sy);
while ((vx=random(7) - 3) == 0);
while ((vy=random(7) - 3) == 0);
// stwarza
ksztalt
ksz_o = new
TImage(Form1);
ksz_o->Parent = Form1;
ksz_o->Left = x0;
ksz_o->Top = y0;
ksz_o->Width = 100;
ksz_o->Height = 100;
ksz_o->AutoSize = true;
ksz_o->Visible = true;
ksz_o->Picture->LoadFromFile("img/sheep.bmp");
}

// KLASA
WILK // // // // // // // // // // // // // // // // // // // //


class Wilk: public


Zwierze
{
    public:
        TImage * ksz_w;
int
masa_wilka;
virtual
void
ruch()
{
    masa_wilka = 0;
x0 += vx;
y0 += vy;
if (x0 >= Sx)
{vx = -vx;
x0 = Sx - 1;}
if (x0 < 0)   {vx=-vx; x0=0;}
if (y0 >= Sy) {vy=-vy; y0=Sy-1;}
if (y0 < 0)   {vy=-vy; y0=0;}
ksz_w->Left=x0;
ksz_w->Top=y0;
}



int zjedzOwce( Owca * owca ) // funkcja, ktora sprawdza czy wilk napotkal owieczke, jesli tak to ja zjada
{
if (spotkanie_owieczki(owca->ksz_o, ksz_w) )
{
owca->ksz_o->Visible=false;
masa_wilka += 1; // gdy wilk zje owce masa wzrasta o 1
return masa_wilka;
}

}


Wilk(); // konstruktor
wilka
~Wilk(void);
};

Wilk::Wilk() // konstruktor
wilka - stworzenie
ksztaltu
i
przypisanie
wartosci
poczatkowych
{
    x0 = random(Sx);
y0 = random(Sy);
vx = 20;
vy = 20;

// stwarza
ksztalt
ksz_w = new
TImage(Form1);
ksz_w->Parent = Form1;
ksz_w->Left = x0;
ksz_w->Top = y0;
ksz_w->Width = 60;
ksz_w->Height = 60;
ksz_w->Visible = true;
ksz_w->AutoSize = true;
ksz_w->Picture->LoadFromFile("img/wolf.bmp");
}

Owca * to[N];
Wilk * tw;

Owca::~Owca()
{
    delete[]
to;
}

Wilk::~Wilk()
{
    delete[]
tw;
}


void
__fastcall
TForm1::Timer1Timer(TObject * Sender)
{

    int
i;
for (i=0; i < N;i++)
{
    to[i]->ruch();
tw->zjedzOwce(to[i]);

}


if (tw->masa_wilka < 3)tw->ruch(); // ruszaj wilkiem dopoki nie zje 3 owiec

}
// ---------------------------------------------------------------------------


void __fastcall TForm1::
    Button2Click(TObject * Sender)
{
    int
i;
for (i=0;i < N;++i)
to[i] = new
Owca;
tw = new
Wilk;
Timer1->Enabled = 1;

}
// ---------------------------------------------------------------------------

   // ---------------------------------------------------------------------------
