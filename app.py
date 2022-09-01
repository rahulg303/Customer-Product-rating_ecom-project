from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle
import bz2file as bz2
import pandas as pd


app = Flask(__name__)

# Load the model
model = pickle.load(open('decision_tree.pkl','rb'))


@app.route("/")
@cross_origin()
def home():
    return render_template("ecom.html")


@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Payment Installments
        payment_installments = float(request.form["Payment Installments"])

        # Payment Value
        payment_value = float(request.form["Payment Value"])

        # Customer Zip Code
        customer_zip_code_prefix= float(request.form["Customer Zip Code"])
       
        # Price
        price = float(request.form["Price"])

        # Freight Value
        freight_value= float(request.form["Freight Value"])


        # Order Status
        order_status = request.form["Order Status"]
        if (order_status == 'Shipped'):
            order_status_shipped = 1
            order_status_canceled = 0
            order_status_processing = 0
            order_status_invoiced = 0
            order_status_other = 0

        elif (order_status == 'Canceled'):
            order_status_shipped = 0
            order_status_canceled = 1
            order_status_processing = 0
            order_status_invoiced = 0
            order_status_other = 0

        elif (order_status == 'Processing'):
            order_status_shipped = 0
            order_status_canceled = 0
            order_status_processing = 1
            order_status_invoiced = 0
            order_status_other = 0

        elif (order_status == 'Invoiced'):
            order_status_shipped = 0
            order_status_canceled = 0
            order_status_processing = 0
            order_status_invoiced = 1
            order_status_other = 0

        elif (order_status == 'Other'):
            order_status_shipped = 0
            order_status_canceled = 0
            order_status_processing = 0
            order_status_invoiced = 0
            order_status_other = 0

        else:
            order_status_shipped = 0
            order_status_canceled = 0
            order_status_processing = 0
            order_status_invoiced = 0
            order_status_other = 0

        # Customer State
        customer_state = request.form["Customer State"]
        if (customer_state == 'RJ'):
            customer_state_RJ = 1
            customer_state_Other = 0

        else:
            customer_state_RJ = 0
            customer_state_Other = 0

        
        prediction=model.predict([[
            payment_installments,          
            payment_value,
            customer_zip_code_prefix,
            price,
            freight_value,
            order_status_canceled,
            order_status_invoiced,
            order_status_processing,
            order_status_shipped,         
            customer_state_RJ    
        ]])

        if prediction == 1:
            output = ("Customer rating is {}".format(prediction),
                      "Customer is not happy, suggest better offer")

        elif prediction == 2:
            output = ("Customer rating is {}".format(prediction),
                      "Customer is not happy, suggest better offer")

        elif prediction == 3:
            output = ("Customer rating is {}".format(prediction), 
                      "Customer is happy")

        elif prediction == 4:
            output = ("Customer rating is {}".format(prediction), 
                      "Customer is happy")
      
        else:
            output = ("Customer rating is {}".format(prediction), 
                      "Customer is satisfied")


        return render_template('ecom.html', output = output)


    return render_template("ecom.html")


if __name__ == "__main__":
    app.run(debug=True)