import java.util.Scanner;

public class electricbill {
    static String name;
    static int unit;
    static double bill; 
    

    static void accept(){
        Scanner SC1=new Scanner(System.in);
        System.out.println("ENTER CUSTOMER NAME");
        name=SC1.next();
        System.out.println("ENTER UNIT ");
        unit=SC1.nextInt();
        SC1.close();
    }
    static  void calculate(){
        if(unit<=100){
            bill=unit*5.76;
        }
        else if(unit>100 && unit<=200){
            bill=100*5.76+(unit-100)*6.50;


        }
        else{
            bill=100*5.76+100*6.50+(unit-200)*7.50;
            double surcharge =bill*(2.5/100);
            bill=bill+surcharge;
        }

}
static void print(){
    System.out.println("name of the consumer"+ name);
    System.out.println("no of unit consumed"+unit);
    System.out.println("bill amount"+bill);
}
public static void main(String[]args){
    electricbill obj=new electricbill();
    obj.accept();
    obj.calculate();
    obj.print();

}
}