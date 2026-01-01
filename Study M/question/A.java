class A {
    void a(){
        System.out.println("Hello 4");
    }
    class Z{
        Z(){
            System.out.println("Hello 6");
        }
    }
    public static void main(String[] args) {
        System.out.println("Hello 1"); 

        A a1 = new A();
        a1.a();
    
    }
    class B {
        B(){
            System.out.println("Hello 2") ;
        }
        static void q(){
            System.out.println("Hello5");
        }
        void q1(){
            System.out.println("Hello5");
        }
        class c{
            c(){
                System.out.println("Hello 3");
            }
        }
    }
}