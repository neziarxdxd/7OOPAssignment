/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/

import java.util.Scanner;
public class Hello {
    public static void main(String []args){
    Scanner input = new Scanner(System.in);
        System.out.print("Enter the Number of Students: ");
            int numberOfStudent = input.nextInt();
        System.out.print("Enter the number of Items");
            int numberOfItems = input.nextInt();
        System.out.print("Enter the Passing Grade: ");
            int passingGrade = input.nextInt();
            // ang galing mo dito 
                int [][] answers = new int [numberOfStudent][numberOfItems];
                
        System.out.println("The " + answers.length +"rows and " + answers[0].length + "column");
            for (int i = 0; i< answers.length; i++){
                for (int j = 0; j < answers[i].length; j++){
                    // dito lalabas kung pangilang student sya at kung pang ilang item yung linagay nya para di mahirapan
                    System.out.println("StudentID -> " +(i+1) + " Item "+(j+1)+":");
                   answers [i][j] = input.nextInt(); 
                }
            }
            // dito iievaluate ang student per item nya 
            int numberOfPassed=0;
            // sa loop na 'to kukunin kugn pangilang student ka 
            for(int getStudent=0; getStudent<answers.length; getStudent++){
                int average=0;
                
                // ito naman yung pkukunin ang average ng student                 
                for (int getGrade=0; getGrade<answers[getStudent].length; getGrade++){
                    average = answers[getStudent][getGrade] + average;                    
                }
                //checheck kung passado or hindi
                if (passingGrade <= (average/numberOfItems)){
                numberOfPassed++;
                }
                System.out.println("Average: "+ (average/numberOfItems));
                
                average=0;            
                
               
                
            }
            System.out.println("PASSED:" +numberOfPassed);
            System.out.println("FAILED:" +(numberOfStudent-numberOfPassed));
            
                
        }
 }
