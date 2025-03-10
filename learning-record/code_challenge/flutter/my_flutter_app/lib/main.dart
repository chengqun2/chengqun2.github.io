import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'config.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'URL Shortener',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.blue),
      ),
      home: const MyHomePage(title: 'URL Shortener'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});
  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

// First, define a proper model class for URL data
class UrlData {
  final String targetUrl;
  final String shortUrl;

  UrlData({required this.targetUrl, required this.shortUrl});

  factory UrlData.fromJson(Map<String, dynamic> json) {
    return UrlData(
      targetUrl: json['target_url']?.toString() ?? '',
      shortUrl: json['short_url']?.toString() ?? '',
    );
  }

  Map<String, String> toMap() {
    return {'target_url': targetUrl, 'short_url': shortUrl};
  }
}

class _MyHomePageState extends State<MyHomePage> {
  final TextEditingController _urlController = TextEditingController();
  // Update the urls list type
  List<UrlData> urls = [];

  // Update _submitUrl method
  Future<void> _submitUrl() async {
    if (_urlController.text.isEmpty) return;

    try {
      final response = await http.post(
        Uri.parse('${Config.apiUrl}/shorten'),
        headers: Config.headers,
        body: jsonEncode({'target_url': _urlController.text}),
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        setState(() {
          urls.add(
            UrlData(
              targetUrl: _urlController.text,
              shortUrl: data['short_url']?.toString() ?? '',
            ),
          );
          _urlController.clear();
        });
      }
    } catch (e) {
      ScaffoldMessenger.of(
        context,
      ).showSnackBar(SnackBar(content: Text('Error: $e')));
    }
  }

  @override
  void initState() {
    super.initState();
    _fetchUrls();
  }

  // Update _fetchUrls method
  Future<void> _fetchUrls() async {
    try {
      final response = await http.get(
        Uri.parse('${Config.apiUrl}/urls'),
        headers: Config.headers,
      );

      if (response.statusCode == 200) {
        final List<dynamic> data = jsonDecode(response.body);
        setState(() {
          urls = data.map((item) => UrlData.fromJson(item)).toList();
        });
      }
    } catch (e) {
      ScaffoldMessenger.of(
        context,
      ).showSnackBar(SnackBar(content: Text('Error fetching URLs: $e')));
    }
  }

  // Update the ListView builder
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(widget.title)),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _urlController,
                    decoration: const InputDecoration(
                      hintText: 'Enter URL to shorten',
                      border: OutlineInputBorder(),
                    ),
                  ),
                ),
                const SizedBox(width: 16),
                ElevatedButton(
                  onPressed: _submitUrl,
                  child: const Text('Shorten'),
                ),
              ],
            ),
            const SizedBox(height: 20),
            Expanded(
              child: ListView.builder(
                itemCount: urls.length,
                itemBuilder: (context, index) {
                  return Card(
                    child: ListTile(
                      title: Text(urls[index].targetUrl),
                      subtitle: Text(urls[index].shortUrl),
                    ),
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
