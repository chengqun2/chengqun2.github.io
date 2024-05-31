echo $request->input('name','default');
dd($request);
var_dump($request);
print_r 
echo "<pre>" var_dump($request);

die 
exit

//route app是views folder  dashboard file 
return redirect(route('app.dashboard'));
    


ConsultantCard.vue

<!-- var_dump(app()->getLocale()); -->

$locale = (app()->getLocale() == 'en') ? '' : str_replace('_', '-', app()->getLocale()).'/';


//string(2) "en"
//var_dump(app()->getLocale());
$supportedLanguagesKeys = LaravelLocalization::getSupportedLanguagesKeys();
//array(3) { [0]=> string(2) "en" [1]=> string(2) "fr" [2]=> string(2) "zh" }
//var_dump($supportedLanguagesKeys);
$locale = (in_array(app()->getLocale(),$supportedLanguagesKeys) 
  && app()->getLocale() == 'en') ? '' :
  str_replace('_', '-', app()->getLocale()).'/';
//string(0) ""
//var_dump($locale);