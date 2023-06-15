model="WizardLM/WizardCoder-15B-V1.0"
temp=0.2
max_len=2048
pred_num=20
num_seqs_per_iter=1

output_path=preds/T${temp}_N${pred_num}

mkdir -p ${output_path}
echo 'Output path: '$output_path
echo 'Model to eval: '$model

python humaneval_gen.py --model ${model} \
  --start_index 0 --end_index 163 --temperature ${temp} \
  --num_seqs_per_iter ${num_seqs_per_iter} --N ${pred_num} --max_len ${max_len} --output_path ${output_path};
