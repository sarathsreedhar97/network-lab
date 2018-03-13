import java.io.*;
import java.net.*;
import java.util.Date;
import java.text.DateFormat;
import java.text.SimpleDateFormat;

class TCPTimeserver {
 public static void main(String argv[]) throws Exception {
  String time,req;
  ServerSocket welcomeSocket = new ServerSocket(6789);

  while (true) {
   Socket connectionSocket = welcomeSocket.accept();
   BufferedReader inFromClient =
    new BufferedReader(new InputStreamReader(connectionSocket.getInputStream()));
   DataOutputStream outToClient = new DataOutputStream(connectionSocket.getOutputStream());
   System.out.println("Server working \n");
   req = inFromClient.readLine();
   System.out.println("Received Time Request: ");
   DateFormat df = new SimpleDateFormat("dd/MM/yy HH:mm:ss");
    Date dateobj = new Date(); 
   time=dateobj.toString();
   time = time +'\n';
    System.out.println(time);
   outToClient.writeBytes(time);
  }
}
}

