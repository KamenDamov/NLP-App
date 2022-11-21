import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    home: HomePage(),
    theme: ThemeData(
      primarySwatch: Colors.cyan,
    ),
  ));
}

class HomePage extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return Scaffold(
      appBar: AppBar(title: Text("Streamline NLP")),
      body: Center(child: Container(
      color: Colors.red,
      width: 100,
      alignment: Alignment.bottomLeft,
      height: 100,
      child: Text("I'm a box"),
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(10)
      ),
      ),),
    );
  }
}