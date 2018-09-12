require 'pp'

require 'sinatra'
require 'sinatra/reloader'

get '/' do
    "Hello world "
end

post '/' do
    params = request.body.read
    pp params
end